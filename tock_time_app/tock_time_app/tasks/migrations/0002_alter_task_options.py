# Generated by Django 5.1.3 on 2024-11-22 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': {('assign_task', 'Can assign task to user')}},
        ),
    ]