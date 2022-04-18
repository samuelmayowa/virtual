from django.urls import path
from .views import *

app_name = 'portfolio'

urlpatterns = [
    path('', view_portfolio, name='portfolio_view'),
    path('details/<slug:slug>/', portfolio_details, name='portfolio_details')
]
