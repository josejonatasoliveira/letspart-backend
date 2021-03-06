# Generated by Django 2.2.6 on 2019-11-24 11:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0004_auto_20191124_0950'),
        ('order', '0005_auto_20191115_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='upload_session',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='evento.UploadSession'),
        ),
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 24, 9, 50, 46, 673464)),
        ),
    ]
