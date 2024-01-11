# Generated by Django 5.0.1 on 2024-01-10 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_daily_log_net_avg'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_log',
            name='Net_Amount',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='daily_log',
            name='Net_Avg',
            field=models.FloatField(blank=True, default='', null=True),
        ),
    ]
