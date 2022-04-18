# Generated by Django 3.1.5 on 2021-01-06 07:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210106_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author_picture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authors_pix', to='blog.about'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 1, 6, 7, 42, 14, 746802, tzinfo=utc)),
        ),
    ]
