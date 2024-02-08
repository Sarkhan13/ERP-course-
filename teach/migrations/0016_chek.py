# Generated by Django 5.0.1 on 2024-01-26 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0015_pay'),
    ]

    operations = [
        migrations.CreateModel(
            name='chek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(blank=True, null=True, verbose_name='ödəməli olduğu son tarix')),
                ('payed', models.BooleanField(blank=True, default=False, null=True, verbose_name='ödənildi')),
                ('paymnt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teach.pay', verbose_name='ödəniş')),
            ],
        ),
    ]