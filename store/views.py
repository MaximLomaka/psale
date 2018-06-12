from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from rest_framework.viewsets import ModelViewSet

from store.forms import UserForm
from store.models import Advertisement, User
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
        password = make_password(form['password'].value())
        print(password)
        form.password = password
        user = form.save(form)

        messages.success(self.request, 'user was created successfully')

        return super().form_valid(form)


'''viewsets for serializers'''


class AdViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
