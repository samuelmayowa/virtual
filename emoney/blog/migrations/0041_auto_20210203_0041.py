# Generated by Django 3.0.11 on 2021-02-02 23:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_auto_20210120_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 2, 2, 23, 41, 15, 644728, tzinfo=utc)),
        ),
    ]
