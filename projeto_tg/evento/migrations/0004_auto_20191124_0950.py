# Generated by Django 2.2.6 on 2019-11-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0003_auto_20191115_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='id_hash',
            field=models.TextField(default='5d75bc1f-1abc-4692-a05f-13fda6f07c1e', unique=True),
        ),
    ]
