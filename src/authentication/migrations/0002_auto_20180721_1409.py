# Generated by Django 2.0.7 on 2018-07-21 12:09

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountverification',
            name='salt',
            field=models.CharField(blank=True, default=authentication.models.get_salt, max_length=32, unique=True),
        ),
    ]
