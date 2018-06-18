'''views for store'''
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView

from rest_framework.viewsets import ModelViewSet

from store.forms import MoneyForm, AdvertisementForm
from store.models import Advertisement, Money
from store.serializers import AdSerializer, UserSerializer


class AdListView(ListView):
    '''list view for all advertisement'''
    template_name = 'store/index.html'
    queryset = Advertisement.objects.all()


class AdDetailView(UpdateView):
    '''view  for change advertisement '''
    template_name = 'store/detail.html'
    model = Advertisement
    form_class = AdvertisementForm

    def form_invalid(self, form):
        return redirect('store:detail', pk=self.kwargs['pk'])

    def form_valid(self, form):
        form.save()
        return redirect('store:detail', pk=self.kwargs['pk'])


class MoneyUpdateView(UpdateView):
    '''view  for change user money balance '''
    model = Money
    template_name = 'store/money_detail.html'
    form_class = MoneyForm
    success_url = reverse_lazy('store:index')


class CreateAd(CreateView):
    '''view  for creating new advertisement'''
    model = Advertisement
    template_name = 'store/create_ad.html'
    fields = ('price', 'description', 'platform', 'games')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user_id = self.kwargs['pk']
        form.save()
        return redirect('store:index')


class AdViewSet(ModelViewSet):
    '''view set serializer for advertisement'''
    queryset = Advertisement.objects.all()
    serializer_class = AdSerializer


class UserViewSet(ModelViewSet):
    '''view set serializer for user'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
