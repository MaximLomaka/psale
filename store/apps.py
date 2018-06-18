'''apps config for store'''
from django.apps import AppConfig


class StoreConfig(AppConfig):
    '''app config'''
    name = 'store'

    def ready(self):
        import store.signals
