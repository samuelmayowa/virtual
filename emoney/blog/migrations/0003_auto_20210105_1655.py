# Generated by Django 3.1.5 on 2021-01-05 15:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210105_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 1, 5, 15, 55, 18, 829414, tzinfo=utc)),
        ),
    ]