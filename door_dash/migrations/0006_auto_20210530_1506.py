# Generated by Django 3.1.6 on 2021-05-30 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('door_dash', '0005_auto_20210530_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doordashstats',
            name='milage',
            field=models.DecimalField(decimal_places=1, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='doordashstats',
            name='net_pay',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
