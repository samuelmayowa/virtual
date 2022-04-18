# Generated by Django 3.0.11 on 2021-01-18 14:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_auto_20210115_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 1, 18, 14, 42, 16, 682222, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
