# Generated by Django 4.0.4 on 2022-06-17 00:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_users',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='profile_image'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]