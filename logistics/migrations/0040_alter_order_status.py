# Generated by Django 4.2.10 on 2024-04-10 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0039_alter_order_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('CONFIRMED', 'confirmed'), ('PICKED UP', 'picked up'), ('IN WAREHOUSE', 'in warehouse'), ('IN TRANSIT', 'in transit'), ('DELIVERED', 'delivered')], max_length=25, null=True),
        ),
    ]