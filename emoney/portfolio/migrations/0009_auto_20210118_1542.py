# Generated by Django 3.0.11 on 2021-01-18 14:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20210115_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2021, 1, 18, 14, 42, 16, 689202, tzinfo=utc)),
        ),
    ]
