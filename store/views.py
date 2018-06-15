from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, UpdateView, DetailView
from rest_framework.viewsets import ModelViewSet

from store.forms import MoneyForm
from store.models import Advertisement, Money
from store.serializers import AdSerializer, UserSerializer


class AdListView(ListView):
    template_name = 'store/index.html'
    queryset = Advertisement.objects.all()


class AdDetailView(ListView):
    template_name = 'store/detail.html'
    model = Advertisement


class MoneyDetailView(UpdateView):
    model = Money
    template_name = 'store/money_detail.html'
    form_class = MoneyForm
    success_url = reverse_lazy('store:index')



'''viewsets for serializers'''


class AdViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
