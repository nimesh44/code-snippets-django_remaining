# Generated by Django 3.1.2 on 2020-10-29 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employeer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
