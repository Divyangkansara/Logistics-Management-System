# Generated by Django 4.2.10 on 2024-03-15 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0023_orders_notify_acc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='freight_type',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='job_category',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='payment_type',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='type',
        ),
    ]
