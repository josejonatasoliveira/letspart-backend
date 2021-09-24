# Generated by Django 2.2.6 on 2019-12-06 19:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20191206_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 6, 17, 59, 19, 973088)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='key',
            field=models.CharField(default='123456789123456', help_text='Chave atualizado do ticket', max_length=16),
        ),
    ]
