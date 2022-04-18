from django.contrib import admin
from .models import Portfolio, PortfolioImage


# Register your models here.
class PortfolioImageAdmin(admin.StackedInline):
    model = PortfolioImage


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PortfolioImageAdmin]

    class Meta:
        model = Portfolio


@admin.register(PortfolioImage)
class PortfolioImageAdmin(admin.ModelAdmin):
    pass
