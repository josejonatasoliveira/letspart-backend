# Generated by Django 2.2.6 on 2019-11-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='id_hash',
            field=models.TextField(default='13910ea6-5c38-44c3-8648-b7abdb7b29e7', unique=True),
        ),
    ]
