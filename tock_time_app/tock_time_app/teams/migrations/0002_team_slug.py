# Generated by Django 5.1.3 on 2024-11-24 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]