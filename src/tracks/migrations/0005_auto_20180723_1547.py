# Generated by Django 2.0.7 on 2018-07-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0004_auto_20180722_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='video_url',
            field=models.URLField(blank=True),
        ),
    ]
