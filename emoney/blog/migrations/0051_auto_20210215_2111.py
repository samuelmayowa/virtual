# Generated by Django 3.0.11 on 2021-02-15 20:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0050_auto_20210215_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 2, 15, 20, 11, 54, 85950, tzinfo=utc)),
        ),
    ]
