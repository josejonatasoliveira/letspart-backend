# Generated by Django 2.2.6 on 2019-11-15 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20191115_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 15, 11, 16, 20, 795259)),
        ),
    ]
