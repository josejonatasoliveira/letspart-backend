# Generated by Django 2.2.6 on 2019-12-06 09:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20191124_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', help_text='Chave atualizado do ticket', max_length=16)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tic_ticket',
            },
        ),
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 6, 7, 27, 18, 908951)),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='order.Ticket'),
        ),
    ]
