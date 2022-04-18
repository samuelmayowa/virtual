from django.contrib import admin
from django.urls import path, include, re_path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('news/', news, name='news'),
    path('contact/', contact, name='contact'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('blog/', include('blog.urls', namespace='blogs')),
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
    path('cryptos/', include('cnewsww.urls', namespace='cryptos')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('newsletter/', include('newsletter.urls')),
    re_path(r'^\.well-known/', include('letsencrypt.urls')),
    path('comments/', include('django_comments_xtd.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
