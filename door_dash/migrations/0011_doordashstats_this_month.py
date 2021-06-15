# Generated by Django 3.1.6 on 2021-05-31 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0001_initial'),
        ('door_dash', '0010_auto_20210530_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='doordashstats',
            name='this_month',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='stat_month', to='months.month'),
        ),
    ]
