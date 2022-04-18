# Generated by Django 3.1.5 on 2021-01-11 02:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20210111_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 1, 11, 2, 2, 41, 907068, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 1, 11, 2, 2, 41, 909061, tzinfo=utc)),
        ),
    ]
