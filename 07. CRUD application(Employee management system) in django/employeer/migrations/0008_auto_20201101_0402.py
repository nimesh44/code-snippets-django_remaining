# Generated by Django 3.1.2 on 2020-11-01 04:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeer', '0007_auto_20201101_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeer',
            name='mobile',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
    ]
