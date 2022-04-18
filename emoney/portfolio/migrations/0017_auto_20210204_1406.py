# Generated by Django 3.0.11 on 2021-02-04 13:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_auto_20210204_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioimage',
            name='slug',
            field=models.SlugField(blank=True, default=None, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2021, 2, 4, 13, 6, 4, 872486, tzinfo=utc)),
        ),
    ]
