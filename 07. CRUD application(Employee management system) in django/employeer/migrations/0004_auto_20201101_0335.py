# Generated by Django 3.1.2 on 2020-11-01 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeer', '0003_remove_employeer_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeer',
            name='address',
            field=models.CharField(default=('netra', 'neupane', 'npn@gmail.com', 'syangja'), max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employeer',
            name='first_name',
            field=models.CharField(default='netra', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employeer',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
    ]
