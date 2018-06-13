from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from rest_framework.viewsets import ModelViewSet

from store.models import Advertisement
from store.serializers import AdSerializer, UserSerializer


class AdListView(ListView):
    template_name = 'store/index.html'
    queryset = Advertisement.objects.all()


class AdDetailView(ListView):
    template_name = 'store/detail.html'
    model = Advertisement


class UserDetailView(DetailView):
    model = User
    template_name = 'store/user-detail.html'


'''viewsets for serializers'''


class AdViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
