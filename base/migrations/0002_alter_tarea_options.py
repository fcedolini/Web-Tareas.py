# Generated by Django 5.1 on 2024-08-19 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tarea',
            options={'ordering': ['completo']},
        ),
    ]
