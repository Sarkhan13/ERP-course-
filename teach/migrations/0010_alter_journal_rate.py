# Generated by Django 5.0.1 on 2024-01-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0009_date_journal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='rate',
            field=models.IntegerField(blank=True, null=True, verbose_name='qiymət'),
        ),
    ]
