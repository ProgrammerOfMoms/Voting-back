# Generated by Django 3.0.5 on 2020-05-13 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('choosing', '0006_auto_20200513_1736'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voter',
            old_name='id_vk',
            new_name='idVK',
        ),
    ]
