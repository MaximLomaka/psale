'''forms for store'''
from django.forms import ModelForm

from store.models import Money, Advertisement


class AdvertisementForm(ModelForm):
    '''form for advertisement'''
    class Meta:
        model = Advertisement
        fields = ['bid', ]


class MoneyForm(ModelForm):
    '''form for money'''
    class Meta:
        model = Money
        fields = ['coins', ]
