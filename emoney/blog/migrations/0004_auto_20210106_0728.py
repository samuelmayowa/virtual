# Generated by Django 3.1.5 on 2021-01-06 06:28

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210105_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author_picture',
            field=models.ForeignKey(blank=True, limit_choices_to='photo', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authors_picture', to='blog.about'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_post_author', to='blog.about'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 1, 6, 6, 28, 50, 989428, tzinfo=utc)),
        ),
    ]
