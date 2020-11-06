# Generated by Django 3.1.2 on 2020-11-03 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100, verbose_name='Título')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('introduction', models.TextField(blank=True, verbose_name='Introducão')),
                ('text', models.TextField(blank=True, verbose_name='Texto')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/images', verbose_name='Imagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'db_table': 'blog',
            },
        ),
    ]
