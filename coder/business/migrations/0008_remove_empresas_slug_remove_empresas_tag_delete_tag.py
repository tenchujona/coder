# Generated by Django 4.0.4 on 2022-07-05 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0007_tag_empresas_slug_empresas_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresas',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='empresas',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]