# Generated by Django 3.1.5 on 2021-01-15 08:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20210115_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2021, 1, 15, 8, 2, 28, 860235, tzinfo=utc)),
        ),
    ]
