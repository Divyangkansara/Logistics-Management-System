# Generated by Django 4.2.10 on 2024-04-04 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0037_order_order_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_number',
            new_name='order_id',
        ),
    ]