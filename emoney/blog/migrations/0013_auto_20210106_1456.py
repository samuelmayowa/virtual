# Generated by Django 3.1.5 on 2021-01-06 13:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210106_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='type',
            new_name='types',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='type',
            new_name='types',
        ),
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 1, 6, 13, 55, 51, 542122, tzinfo=utc)),
        ),
    ]