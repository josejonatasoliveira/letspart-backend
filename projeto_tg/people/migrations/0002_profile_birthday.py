# Generated by Django 2.2.6 on 2019-11-19 00:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 18, 22, 42, 32, 368446), verbose_name='Data de Nascimento'),
        ),
    ]
