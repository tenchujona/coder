# Generated by Django 4.0.4 on 2022-06-10 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_rename_username_accounts_username_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Accounts',
        ),
    ]
