# Generated by Django 3.0.5 on 2020-05-13 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choosing', '0005_voter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voter',
            name='user',
        ),
        migrations.AddField(
            model_name='voter',
            name='firstName',
            field=models.CharField(default='unknown', max_length=20),
        ),
        migrations.AddField(
            model_name='voter',
            name='id_vk',
            field=models.CharField(default=-1, max_length=20),
        ),
        migrations.AddField(
            model_name='voter',
            name='lastName',
            field=models.CharField(default='unknown', max_length=20),
        ),
    ]