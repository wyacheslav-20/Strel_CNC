from django.urls import path
from .views import BBLoginView
from .views import index
from .views import other_page
from .views import profile
from .views import BBLogoutView
from .views import ChangeUserinfoView
from .views import BBPasswordChangeView
from .views import RegisterUserView, RegisterDoneView
from .views import user_activate
app_name = 'main'

urlpatterns = [
path( 'acoounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
path( 'acoounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
path ('acoounts/register/', RegisterUserView.as_view (), name='register'),
path('<str:page>', other_page, name='other'),        
path('', index, name='index'),
path('accounts/login/', BBLoginView.as_view(), name='login'),
path('accounts/profile/', profile, name='profile'),
path('accounts/logout/', BBLogoutView.as_view (), name='logout'),
path( 'acoounta/profile/change/', ChangeUserinfoView.as_view(), name='profile_change'),
path('accounts/profile/', profile, name='profile'),
path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
]