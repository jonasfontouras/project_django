# Generated by Django 3.1.2 on 2020-11-06 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='introduction',
            field=models.TextField(blank=True, verbose_name='Descrição'),
        ),
    ]
