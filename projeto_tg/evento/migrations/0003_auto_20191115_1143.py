# Generated by Django 2.2.6 on 2019-11-15 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0002_auto_20191115_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='id_hash',
            field=models.TextField(default='c3ae62f2-c153-4780-b4d7-402b4d370056', unique=True),
        ),
    ]
