# Generated by Django 3.0.2 on 2020-02-06 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200204_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30, verbose_name='Aвтop')),
                ('content', models.TextField(verbose_name='Coдepжaниe')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Выводить на экран?')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликован')),
                ('st', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.St', verbose_name='Объявление')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-created_at'],
            },
        ),
    ]
