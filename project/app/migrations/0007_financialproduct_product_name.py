# Generated by Django 3.1.3 on 2020-11-27 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201126_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialproduct',
            name='product_name',
            field=models.CharField(default='unnamed', max_length=50),
        ),
    ]
