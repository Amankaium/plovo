# Generated by Django 3.2 on 2021-06-21 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='county',
            new_name='country',
        ),
    ]
