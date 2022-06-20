# Generated by Django 4.0.4 on 2022-06-17 01:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0021_data_users_image_delete_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_users',
            name='image',
            field=models.ImageField(default='default/anonymous-user.png', upload_to='profile_image'),
        ),
        migrations.AlterField(
            model_name='data_users',
            name='user',
            field=models.OneToOneField(max_length=20, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
