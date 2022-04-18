from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils import timezone
from django.utils.text import slugify


def get_image_filename(instance, filename):
    id = instance.portfolio.id
    return "media_root/static/media/portfolio/%s" % (id)


project_choices = (
    ('Machine Learning', (
        ('ai', 'Artificial Intelligence'),
    )),
    ('Buy and Sell', (
        ('cryptos', 'Cryptocurrencies'),
    )
    ),
    (
        'Deploy', (
            ('web', 'Web Deployment '),
        )
    ),
)

categorybag = [
    ('cryptos', 'Cryptocurrency'),
    ('ai', 'Artificial Intelligence'),
    ('web', 'Web Development'),
]


class Portfolio(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, null=True, blank=True, default=None)
    description = CKEditor5Field('Text', null=True)
    category = models.CharField(choices=categorybag, max_length=50, null=True)
    client = models.CharField(null=True, max_length=50, blank=True)
    project_date = models.DateTimeField(auto_now_add=False, null=True)
    website = models.URLField(
        null=True, max_length=100, blank=True, default='No Website')
    featured = models.ImageField(
        upload_to="media_root/static/media/portfolio", blank=True)
    limitation = models.CharField(
        null=True, max_length=50, choices=project_choices)
    published_date = models.DateTimeField(timezone.now(), auto_now_add=True)

    def __str__(self):
        return self.title

    # the following makes sure that slug is included
    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(Portfolio, self).save(*args, **kwargs)

    def summary(self):
        return self.description[:100]+' ...'

    def summary2(self):
        return self.description[:300]+' ...'


class PortfolioImage(models.Model):
    portfolio_name = models.ForeignKey(
        Portfolio, default=None, on_delete=models.CASCADE, related_name='portfolios')
    slug = models.SlugField(unique=True, null=True, blank=True, default=None)
    slideshow = models.FileField(
        upload_to='media_root/static/media/portfolio/slideshow')

    def __str__(self):
        return self.portfolio_name.title

    def save(self, *args, **kwargs):
        if not self.slug and self.portfolio_name:
            self.slug = slugify(self.portfolio_name)
        super(PortfolioImage, self).save(*args, **kwargs)
