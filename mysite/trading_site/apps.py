from django.apps import AppConfig


class TradingSiteConfig(AppConfig):
    name = 'trading_site'

    def ready(self):
        from . import signals