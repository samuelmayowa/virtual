from django_comments_xtd.admin import XtdCommentsAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from .models import Blog, Message, Tag, Category, Testimonials, About


admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Testimonials)
admin.site.register(About)
admin.site.register(Message)
