# Generated by Django 3.2 on 2021-05-07 14:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0005_alter_dish_calories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='calories',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(10000)]),
        ),
    ]
