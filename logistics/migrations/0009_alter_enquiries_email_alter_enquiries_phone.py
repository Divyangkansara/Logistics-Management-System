# Generated by Django 4.2.10 on 2024-03-06 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0008_alter_enquiries_priority_tags_alter_enquiries_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiries',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='enquiries',
            name='phone',
            field=models.CharField(default='1212121212', max_length=15),
        ),
    ]
