# Generated by Django 3.1.6 on 2021-05-30 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoorDashStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gasCost', models.DecimalField(decimal_places=2, max_digits=1000, null=True)),
                ('netPay', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('milage', models.DecimalField(decimal_places=1, max_digits=1000)),
                ('date', models.DateField()),
                ('otherCosts', models.DecimalField(decimal_places=2, max_digits=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]