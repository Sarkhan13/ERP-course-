# Generated by Django 5.0.1 on 2024-02-13 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0024_alter_teacher_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='techerid',
        ),
    ]