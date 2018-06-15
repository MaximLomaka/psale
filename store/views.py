from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
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


class GetMonetView(UpdateView):
    model = Money
    template_name = 'store/user-detail.html'
    fields = ('coins',)
    success_url = '/'


class UserDetailView(FormView):
    model = Money
    template_name = 'store/user-detail.html'
    form_class = MoneyForm

    def form_valid(self, form):
        if int(form['coins'].value()) > 0:
            form.save()
            return redirect('store:user_detail')


'''viewsets for serializers'''


class AdViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
