# Generated by Django 3.0.11 on 2021-02-02 23:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20210120_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='category',
            field=models.CharField(choices=[('Cryptocurrency', 'Cryptocurrency'), ('Deep Learning', 'DL'), ('Machine Learning', 'ML'), ('Web Development', 'WD')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='client',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='project_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='website',
            field=models.URLField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2021, 2, 2, 23, 41, 15, 695480, tzinfo=utc)),
        ),
    ]
