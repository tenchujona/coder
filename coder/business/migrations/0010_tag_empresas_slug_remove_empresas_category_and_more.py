# Generated by Django 4.0.4 on 2022-07-05 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0009_remove_empresas_category_empresas_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='empresas',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True, unique=True),
        ),
        migrations.RemoveField(
            model_name='empresas',
            name='category',
        ),
        migrations.AddField(
            model_name='empresas',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Empresas', to='business.category'),
        ),
        migrations.AddField(
            model_name='empresas',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tag_category', to='business.tag'),
        ),
    ]
