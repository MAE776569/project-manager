# Generated by Django 2.0.7 on 2018-07-24 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0006_auto_20180724_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]
