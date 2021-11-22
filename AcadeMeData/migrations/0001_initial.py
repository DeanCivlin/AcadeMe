# Generated by Django 3.2.8 on 2021-11-22 17:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('university_id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)])),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
    ]
