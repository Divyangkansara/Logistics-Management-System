# Generated by Django 4.2.10 on 2024-04-11 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0040_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(),
        ),
    ]
