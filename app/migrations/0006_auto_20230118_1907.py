# Generated by Django 3.2.16 on 2023-01-18 19:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_auto_20230118_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='followers',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
