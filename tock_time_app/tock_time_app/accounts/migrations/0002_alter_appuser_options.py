# Generated by Django 5.1.3 on 2024-11-20 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appuser',
            options={'verbose_name': 'User account', 'verbose_name_plural': 'User accounts'},
        ),
    ]
