# Generated by Django 5.0.1 on 2024-02-03 10:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0017_chek_created_date_chek_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chek',
            name='paymnt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cheks', to='teach.pay', verbose_name='ödəniş'),
        ),
    ]
