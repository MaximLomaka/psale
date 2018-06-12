from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from rest_framework.viewsets import ModelViewSet

from store.forms import UserForm
from store.models import Advertisement
from store.serializers import AdSerializer, UserSerializer


class AdListView(ListView):
    template_name = 'store/index.html'
    queryset = Advertisement.objects.all()


class AdDetailView(ListView):
    template_name = 'store/detail.html'
    model = Advertisement


class CreateUserView(FormView):
    form_class = UserForm
    template_name = 'store/registration.html'

    success_url = reverse_lazy('store:index')

    def form_valid(self, form):
        print(form)
        # password = make_password(form['password'].value())
        # print(password)
        # form.password = password
        form.save()
        messages.success(self.request, 'user was created successfully')

        return super().form_valid(form)

    '''sign in view for log in user'''


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'store/login.html')


'''viewsets for serializers'''


class AdViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
