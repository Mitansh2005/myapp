# Generated by Django 5.0.1 on 2024-01-07 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_alter_daily_log_sell_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_log',
            name='Sell_Amount',
            field=models.FloatField(default='0', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='daily_log',
            name='Sell_Date',
            field=models.DateField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='daily_log',
            name='Sell_Quantity',
            field=models.IntegerField(default='0', null=True),
        ),
        migrations.AlterField(
            model_name='daily_log',
            name='Sell_Rate',
            field=models.FloatField(default='0', null=True),
        ),
    ]