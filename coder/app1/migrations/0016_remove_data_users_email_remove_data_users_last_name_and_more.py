# Generated by Django 4.0.4 on 2022-06-11 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_rename_username_data_users_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data_users',
            name='email',
        ),
        migrations.RemoveField(
            model_name='data_users',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='data_users',
            name='name',
        ),
    ]
