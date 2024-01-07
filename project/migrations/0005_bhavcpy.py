# Generated by Django 5.0.1 on 2024-01-05 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_daily_log_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bhavcpy',
            fields=[
                ('Symbol', models.CharField(max_length=10)),
                ('Series', models.CharField(max_length=2)),
                ('Open_Price', models.FloatField()),
                ('High_Price', models.FloatField()),
                ('Low_Price', models.FloatField()),
                ('Close_Price', models.FloatField()),
                ('Last', models.FloatField()),
                ('Prevclose', models.FloatField()),
                ('Tottrdqty', models.IntegerField()),
                ('Tottrdval', models.FloatField()),
                ('Timestap', models.DateField()),
                ('Total_Trades', models.IntegerField()),
                ('Isin', models.CharField(max_length=12, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['Symbol'],
            },
        ),
    ]