# Generated by Django 3.0.5 on 2020-05-13 05:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id_vk', models.CharField(max_length=50, unique=True, verbose_name='Логин (id_vk)')),
                ('firstName', models.CharField(max_length=20, verbose_name='Имя')),
                ('lastName', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('is_social', models.BooleanField(default=True, verbose_name='Зарегистрирован через соц. сеть')),
                ('is_active', models.BooleanField(default=True, verbose_name='Аккаунт действует')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Сотрудник')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
