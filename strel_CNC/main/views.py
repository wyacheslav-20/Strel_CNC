from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import PasswordChangeView
import pdb
from .models import AdvUser
from .forms import ChangeUserinfoForm
from .forms import RegisterUserForm
from django.views.generic.base import TemplateView
from django.core.signing import BadSignature
from django.views.generic.edit import CreateView

from .utilities import signer

class BBLoginView(LoginView):
    template_name = 'main/login.html'
def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))
def index(request) :
    return render(request, 'main/index.html')
@login_required
def profile(request):
    return render(request, 'main/profile.html')
class BBLogoutView(LoginRequiredMixin, LogoutView):
    #pdb.set_trace()
    #input()
    template_name = 'main/logout.html'
    
class ChangeUserinfoView(SuccessMessageMixin, LoginRequiredMixin,
                         UpdateView) :
    model = AdvUser
    template_name = 'main/change_user_info.html'
    form_class = ChangeUserinfoForm
    success_url = reverse_lazy('main:profile')
    success_message = 'личные данные пользователя изменены'
    def dispatch(self, request, *args, **kwargs):
        self . user_id = request.user.pk
        return super() .dispatch(request, *args, **kwargs)
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
            return get_object_or_404(queryset, pk=self.user_id)
class BBPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin,
                           PasswordChangeView) :
    template_name = 'main/password_change.html' 
    success_url = reverse_lazy('main:profile')
    success_message = 'Пароль пользователя изменен'
    

class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    succes_url = reverse_lazy('main:register_done')
    
class RegisterDoneView(TemplateView):
    template_name = 'main/ register_done.html'
    
def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'main/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'main/user is activated.html'
    else:
        template = 'main/ac tivation done.html'
        user.is_active = True
        user.is_activated = True
        user. save ()
    return render(request, template)


