# Generated by Django 4.2.10 on 2024-03-06 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0005_rename_dimentions_approved_quotations_dimensions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiries',
            name='contact_person',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='enquiries',
            name='sales_person',
            field=models.CharField(max_length=50),
        ),
    ]