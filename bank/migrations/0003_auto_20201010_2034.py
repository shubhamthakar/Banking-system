# Generated by Django 2.2.16 on 2020-10-10 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_auto_20201010_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address2',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address3',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
