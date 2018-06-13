# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView

from auth.forms import UserCreate, UserLogin


class UserSignUpView(CreateView):
    model = User
    form_class = UserCreate
    template_name = 'auth/singin.html'

    # def form_invalid(self, form):
    #     if form['password'] is not form['password']:
    #

    def form_valid(self, form):
        print('pass= ' + form['password'].value())
        print('comf= ' + form['confirm_password'].value())
        user = form.save(commit=False)

        user.set_password(form['password'])
        # save user with hashed password
        form.save()
        login(self.request, user)
        return redirect('store:index')


class UserLoginView(LoginView):
    authentication_form = UserLogin
    template_name = 'auth/singin.html'
