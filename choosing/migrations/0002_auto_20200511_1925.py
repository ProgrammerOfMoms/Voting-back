# Generated by Django 3.0.5 on 2020-05-11 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choosing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_ip', models.CharField(max_length=100)),
                ('isVote', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='candidate',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
