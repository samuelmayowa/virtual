# Generated by Django 3.0.11 on 2021-02-04 10:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_auto_20210203_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2021, 2, 4, 10, 42, 26, 604827, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='portfolioimage',
            name='slideshow',
            field=models.FileField(upload_to='media_root/static/media/portfolio/slideshow'),
        ),
    ]
