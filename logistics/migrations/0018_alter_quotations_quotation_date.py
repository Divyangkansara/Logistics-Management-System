# Generated by Django 4.2.10 on 2024-03-11 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0017_alter_approved_quotations_sales_person_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotations',
            name='quotation_date',
            field=models.DateTimeField(),
        ),
    ]