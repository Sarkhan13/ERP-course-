# Generated by Django 5.0.1 on 2024-01-21 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0010_alter_journal_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='journal',
        ),
    ]
