# Generated by Django 5.0.1 on 2024-02-17 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0027_alter_student_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chek',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='date',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='journal',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pay',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
