# Generated by Django 3.0.11 on 2021-01-18 16:35

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments_xtd', '0008_auto_20200920_2037'),
        ('blog', '0038_auto_20210118_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 1, 18, 16, 35, 45, 535025, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='MyCustomComment',
            fields=[
                ('xtdcomment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_comments_xtd.XtdComment')),
                ('title', models.CharField(max_length=256)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customcomment', to='blog.Blog')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'ordering': ('submit_date',),
                'permissions': [('can_moderate', 'Can moderate comments')],
                'abstract': False,
            },
            bases=('django_comments_xtd.xtdcomment',),
        ),
    ]
