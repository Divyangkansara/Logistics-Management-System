# Generated by Django 4.2.10 on 2024-04-04 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0033_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='enquiry',
        ),
        migrations.AddField(
            model_name='order',
            name='quotation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logistics.quotation'),
        ),
    ]
