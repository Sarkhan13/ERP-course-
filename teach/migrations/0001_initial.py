# Generated by Django 5.0.1 on 2024-01-09 19:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='müəllimin adı')),
                ('surname', models.CharField(max_length=100, verbose_name='müəllimin soyadı')),
                ('birthday', models.IntegerField(verbose_name='təvəllüdü')),
                ('startdate', models.IntegerField(verbose_name='işə başladığı tarix')),
                ('salary', models.IntegerField(verbose_name='maaş')),
                ('profession', models.CharField(max_length=100, verbose_name='ixtisas')),
                ('workpractice', models.TextField(verbose_name='iş təcrubəsi')),
                ('profilepic', models.ImageField(upload_to='', verbose_name='profil şəkli')),
                ('techerid', models.IntegerField(verbose_name='Müəllim İD-si')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]