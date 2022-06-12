# Generated by Django 4.0.4 on 2022-06-12 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0017_delete_data_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=9)),
                ('birthday', models.DateField()),
                ('user', models.OneToOneField(max_length=20, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
