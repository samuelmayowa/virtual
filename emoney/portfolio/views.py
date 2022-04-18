from django.shortcuts import render, get_object_or_404
from .models import Portfolio, PortfolioImage

# Create your views here.


def view_portfolio(request):
    portfolio = Portfolio.objects.all()
    ai_portfolio = portfolio.filter(
        limitation='ai')[:12]
    cryptos_portfolio = portfolio.filter(
        limitation='cryptos')[:12]
    forex_portfolio = portfolio.filter(
        limitation='web')[:12]
    template = 'portfolio/portfolio.html'
    context = {
        'portfolio': portfolio,
        'cryp_port': cryptos_portfolio,
        'deploy_port': forex_portfolio,
        'aiport': ai_portfolio,
    }
    return render(request, template, context)


def portfolio_details(request, slug):
    full_portfolio = get_object_or_404(Portfolio, slug=slug)
    port_slide = full_portfolio.portfolios.all()
    template = 'portfolio/portfolio_details.html'
    context = {'port_details': full_portfolio, 'port_slide': port_slide}
    return render(request, template, context)
