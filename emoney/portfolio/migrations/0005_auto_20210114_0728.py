# Generated by Django 3.1.5 on 2021-01-14 06:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20210111_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2021, 1, 14, 6, 28, 35, 391890, tzinfo=utc)),
        ),
    ]
