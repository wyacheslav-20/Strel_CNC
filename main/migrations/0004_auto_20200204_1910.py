# Generated by Django 3.0.2 on 2020-02-04 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_additionalimage_st'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubric',
            name='name',
            field=models.CharField(db_index=True, max_length=20, null=True, unique=True, verbose_name='Haзвaниe'),
        ),
        migrations.AlterField(
            model_name='st',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.SubRubric', verbose_name='Pyбpикa'),
        ),
    ]
