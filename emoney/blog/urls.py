
from django.urls import path
from .views import *

app_name = 'blogurls'

urlpatterns = [
    path('', allblogs, name='blog'),
    path('details/<slug:slug>/', blogdetails, name='blog_details'),
    path('cat/<slug:category_slug>/',
         allblogs, name='blog_list_category'),
    path('tags/<slug:tag_slug>/', allblogs, name='tag_list'),
    path('search/', SearchListView.as_view(), name='search'),
]
