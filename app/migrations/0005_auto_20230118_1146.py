# Generated by Django 3.2.16 on 2023-01-18 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_userinfo_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'ordering': ['-user__date_joined']},
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='created_on',
        ),
    ]
