# Generated by Django 4.0.4 on 2022-06-17 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0032_remove_data_users_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresas',
            name='category',
        ),
    ]
