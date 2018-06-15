from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, PasswordInput

from store.models import Money, Advertisement


class AdForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = ['bid', ]


class MoneyForm(ModelForm):
    class Meta:
        model = Money
        fields = ['coins', ]
