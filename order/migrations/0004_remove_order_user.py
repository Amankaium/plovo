# Generated by Django 3.2.3 on 2021-05-26 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_additiondish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]