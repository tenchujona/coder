# Generated by Django 4.0.4 on 2022-07-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0055_delete_data_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
