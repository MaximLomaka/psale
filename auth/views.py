# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import CreateView

from auth.forms import UserCreate


class UserSignUpView(CreateView):
    model = User
    form_class = UserCreate
    template_name = 'auth/singin.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('store:index')
