# Generated by Django 3.0.11 on 2021-02-03 20:34

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_auto_20210203_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2021, 2, 3, 20, 34, 26, 858826, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slideshow', models.FileField(upload_to=portfolio.models.get_image_filename)),
                ('portfolio_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio.Portfolio')),
            ],
        ),
    ]
