# Generated by Django 5.1.3 on 2024-12-05 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_personaltask_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamtask',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
