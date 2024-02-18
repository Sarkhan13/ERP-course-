# Generated by Django 5.0.1 on 2024-02-17 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0028_alter_chek_updated_date_alter_date_updated_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='month_statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_count', models.IntegerField(verbose_name='tələbə sayı')),
                ('month', models.IntegerField(verbose_name='Ay')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
