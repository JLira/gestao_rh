# Generated by Django 3.2 on 2024-01-22 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0003_auto_20240122_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionarios',
            name='departamentos',
        ),
        migrations.RemoveField(
            model_name='funcionarios',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='funcionarios',
            name='owner',
        ),
    ]
