# Generated by Django 4.2.10 on 2024-04-04 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0035_remove_enquirie_priority_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='enquiry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logistics.enquirie'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('PENDING', 'Pending'), ('IN WAREHOUSE', 'in warehouse'), ('OUT FOR DELIVERY', 'out for delivery'), ('DELIVERED', 'delivered')], max_length=25, null=True),
        ),
    ]
