

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'Accepted'), (1, 'Completed'), (2, 'Canceled'), (3, 'Deleted')], default=0),
        ),
    ]
