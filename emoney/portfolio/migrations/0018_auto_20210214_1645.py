# Generated by Django 3.0.11 on 2021-02-14 15:45

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_auto_20210204_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='limitation',
            field=models.CharField(choices=[('Machine Learning', (('ml', 'Machine Learning'),)), ('Deep Learning', (('dl', 'Deep Learning'),)), ('Buy and Sell', (('cryptos', 'Cryptocurrencies'),)), ('Deploy', (('deploy', 'Deployment '),))], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2021, 2, 14, 15, 45, 41, 667630, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='portfolioimage',
            name='portfolio_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='portfolios', to='portfolio.Portfolio'),
        ),
    ]
