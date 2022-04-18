from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.safestring import mark_safe
from django_ckeditor_5.fields import CKEditor5Field
from django.db import models
from django_comments_xtd.models import XtdComment


# this filters the unpublished contents from the published ones
class ArticleFilter(models.Manager):
    def active(self, *args, **kwargs):
        return super(ArticleFilter, self).filter(draft=False).filter(publish__lte=timezone.now())


class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())


class Blog(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True, null=True)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, null=True)
    content = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to='media_root/static/media/blog_pix')
    published_date = models.DateTimeField(timezone.now())
    author = models.ForeignKey(
        'About', null=True, on_delete=models.CASCADE)
    draft = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog Posts'

    # the following returns the expected content for the summary

    def summary(self):
        return self.content[:400]

    objects = ArticleFilter()

    def summary2(self):
        return mark_safe(self.content[:100])
    # the following beautify the date displayed

    def pub_date_pretty(self):
        return self.published_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title

    # the following makes sure that slug is included
    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    # this makes it possible for the created article to find the right path to the database
    def get_absolute_url(self):
        return reverse("blogurls:blog_details", kwargs={"slug": self.slug})

    def get_markdown(self):
        body = self.body
        markdown_text = markdown(body)
        return mark_safe(markdown_text)

    # def approved_comment(self):
    #     qs = self.comment.filter(approved_comments=True)
    #     return qs


# list of available tags
tagbag = (
    ('Artificial Intelligence', (
        ('Machine Learning', 'ML'),
        ('Deep Learning', 'DL'),
        ('Computer Vision', 'CV'),
    )),
    ('Deployment', (
        ('Django', 'DJ'),
        ('Streamlit', 'ST'),
    )),
    ('Buy and Sell', (
        ('BTC', 'buy btc'),
        ('Ethereum(ETH)', 'buy ethereum'),
        ('Ripple(XRP)', 'buy ripple'),
        ('EOS(EOS)', 'buy eos'),
        ('DASH(DASH)', 'buy dash'),
        ('Binance Coin(BNB)', 'buy binance coin'),
        ('Monero(XMR)', 'buy monero'),
        ('Steem(STEEM)', 'buy steem'),
        ('Cardano(ADA)', 'buy cardano'),
        ('Neo(NEO)', 'buy neo'),
        ('Litecoin(LTC)', 'buy litecoin'),
        ('Tron(TRX)', 'buy tron'),
    )
    ),
    ('Digital Wallet', (
        ('Hardware wallet', 'hardware wallet'),
        ('Bitcoin wallet', 'BTC'),
        ('Ethereum Wallet', 'ethereum wallet'),
    )
    ),
    ('Crypto Exchange', (
        ('Name of exchange', 'name of exchange'),
    )
    ),
    ('Mining Guide', (
        ('BTC mining', 'btc mining'),
    )
    ),
    (
        'Forex Education', (
            ('How to trade Forex', 'how to trade forex'),
        )
    ),

    (
        'Forex Trading', (
            ('Technical Analysis', 'technical'),
            ('Psychological Analysis', 'Psychology'),
            ('Trading System', 'trading system'),
        )
    ),
    ('Passive Income', 'Passive Income'),
)
categorybag = [('Investment', 'investment'), ('Education', 'educ'),
               ('Money', 'money'), ('Risk', 'risk')]


class Tag(models.Model):
    types = models.CharField(max_length=50, choices=tagbag)
    slug = models.SlugField(unique=True, blank=True, null=True)

    # the following makes sure that slug is included
    def save(self, *args, **kwargs):
        if not self.slug and self.types:
            self.slug = slugify(self.types)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.types


class Category(models.Model):
    types = models.CharField(max_length=50, choices=categorybag)
    slug = models.SlugField(unique=True, blank=True, null=True)

    # the following makes sure that slug is included
    def save(self, *args, **kwargs):
        if not self.slug and self.types:
            self.slug = slugify(self.types)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.types

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


# the following handles about models


class About(models.Model):
    name = models.OneToOneField(
        User, related_name='about_name', on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True,
                              upload_to='media_root/static/media/people')
    about = CKEditor5Field(max_length=3000)

    def __str__(self):
        return 'Information about {}'.format(self.name)

    class Meta:
        verbose_name = 'About'


class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='media_root/static/media/testimonials', null=True)
    testimony = models.TextField(max_length=500)

    def __str__(self):
        return 'Testimony from {}'.format(self.name)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'


class Message(models.Model):
    your_name = models.CharField(max_length=100)
    your_email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return 'Message from {}'.format(self.your_name.upper())
