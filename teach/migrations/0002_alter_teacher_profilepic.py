# Generated by Django 5.0.1 on 2024-01-10 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='profilepic',
            field=models.ImageField(upload_to='profilepic/', verbose_name='profil şəkli'),
        ),
    ]