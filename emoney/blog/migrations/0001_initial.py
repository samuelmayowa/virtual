# Generated by Django 3.1.5 on 2021-01-05 15:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Breaking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_news', models.TextField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Investment', 'investment'), ('Education', 'educ'), ('Money', 'money'), ('Rist', 'risk')], max_length=50)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=100)),
                ('your_email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Buy and Sell', (('Buy BTC', 'buy btc'), ('Buy Ethereum(ETH)', 'buy ethereum'), ('Buy Ripple(XRP)', 'buy ripple'), ('Buy EOS(EOS)', 'buy eos'), ('Buy DASH(DASH)', 'buy dash'), ('Buy Binance Coin(BNB)', 'buy binance coin'), ('Buy Monero(XMR)', 'buy monero'), ('Buy Steem(STEEM)', 'buy steem'), ('Buy Cardano(ADA)', 'buy cardano'), ('Buy Neo(NEO)', 'buy neo'), ('Buy Litecoin(LTC)', 'buy litecoin'), ('Buy Tron(TRX)', 'buy tron'))), ('Digital Wallet', (('Hardware wallet', 'hardware wallet'), ('Bitcoin wallet', 'BTC'), ('Ethereum Wallet', 'ethereum wallet'))), ('Crypto Exchange', (('Name of exchange', 'name of exchange'),)), ('Mining Guide', (('BTC minig', 'btc mining'),)), ('Forex Education', (('How to trade Forex', 'how to trade forex'),)), ('Forex Trading', (('Technical Analysis', 'technical'), ('Psychological Analysis', 'Psychology'), ('Trading System', 'trading system'))), ('Passive Income', 'Passive Income')], max_length=50)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='static/media/testimonials')),
                ('testimony', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('content', django_ckeditor_5.fields.CKEditor5Field(max_length=8000)),
                ('image', models.ImageField(upload_to='static/media/blog_pix')),
                ('published_date', models.DateTimeField(verbose_name=datetime.datetime(2021, 1, 5, 15, 52, 20, 755005, tzinfo=utc))),
                ('draft', models.BooleanField(default=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_post_author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
                ('tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.tag')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog Posts',
            },
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='static/media/people_pix')),
                ('about', django_ckeditor_5.fields.CKEditor5Field(max_length=3000)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'About',
            },
        ),
    ]
