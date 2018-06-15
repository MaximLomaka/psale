from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, UpdateView, DetailView, CreateView
from rest_framework.viewsets import ModelViewSet

from store.forms import MoneyForm, AdForm
from store.models import Advertisement, Money
from store.serializers import AdSerializer, UserSerializer


class AdListView(ListView):
    template_name = 'store/index.html'
    queryset = Advertisement.objects.all()


class AdDetailView(UpdateView):
    template_name = 'store/detail.html'
    model = Advertisement
    form_class = AdForm

    def form_invalid(self, form):
        print(form)
        print('ff')
        return redirect('store:detail', pk=self.kwargs['pk'])

    def form_valid(self, form):
        print(form)
        form.save()
        return redirect('store:detail', pk=self.kwargs['pk'])


class MoneyUpdateView(UpdateView):
    model = Money
    template_name = 'store/money_detail.html'
    form_class = MoneyForm
    success_url = reverse_lazy('store:index')


'''viewsets for serializers'''


class CreateAd(CreateView):
    model = Advertisement
    template_name = 'store/create_ad.html'
    fields = ('price', 'description', 'platform', 'games')

    def form_valid(self, form):
        print(form)
        user = form.save(commit=False)
        user.user_id = self.kwargs['pk']
        form.save()
        return redirect('store:index')


class AdViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
