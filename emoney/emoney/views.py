from django.shortcuts import render, get_object_or_404
import json
import requests
from blog.models import *
from portfolio.models import *
# from newspaper import news_pool
# import newspaper


def index(request):
    '''The following is from the cryptocompare'''

    api_key = 'b482ab1030160854bf97c37a675709ca6c619767319ad71ee20a4a085b30dd38'
    api_request = requests.get(
        "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"+'&api_key='+api_key)
    api_content = json.loads(api_request.content)
    blogging = Blog.objects.filter(draft=False)[:12]
    portfolio = Portfolio.objects.all()
    ai_portfolio = portfolio.filter(
        limitation='ai')[:12]
    cryptos_portfolio = portfolio.filter(
        limitation='cryptos')[:12]
    forex_portfolio = portfolio.filter(
        limitation='web')[:12]

    page = request.GET.get('page')
    content = {
        'port': portfolio,
        'cryp_port': cryptos_portfolio,
        'web': forex_portfolio,
        'aiport': ai_portfolio,
        'blogging': blogging,
        'about': about,
        'crypto_api': api_content['Data'][:12],
    }
    templates = 'index.html'
    return render(request, templates, content)


def about(request):
    templates = 'about.html'
    return render(request, templates)


def news(request):
    """The main news"""

    ai_news = newspaper.build('https://artificialintelligence-news.com/')
    for i in ai_news.articles:
        print(i.url)

    '''The following is from the cryptocompare'''
    # this fetch the news update
    api_key = 'b482ab1030160854bf97c37a675709ca6c619767319ad71ee20a4a085b30dd38'
    api_request = requests.get(
        "https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key="+api_key)
    api_content = json.loads(api_request.content)

    content = {
        'crypto_api': api_content['Data'][:12],
        'ai': ai_news,
    }
    templates = 'news.html'
    return render(request, templates, content)


def contact(request):
    templates = 'contact.html'
    return render(request, templates)


def signup(request):
    templates = 'sign-up.html'
    return render(request, templates)


def login(request):
    templates = 'login.html'
    return render(request, templates)


def single(request):
    templates = 'single.html'
    return render(request, templates)
