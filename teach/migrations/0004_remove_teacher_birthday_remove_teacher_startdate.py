# Generated by Django 5.0.1 on 2024-01-11 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0003_teacher_birth_teacher_start'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='startdate',
        ),
    ]
