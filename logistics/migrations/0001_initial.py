# Generated by Django 4.2.10 on 2024-03-01 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('contact', models.CharField(max_length=15, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('postal', models.IntegerField(max_length=10)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='customer_photos/')),
            ],
        ),
    ]
