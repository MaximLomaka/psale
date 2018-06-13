# Create your views here.
from django.contrib.auth import login, authenticate
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
        user = form.save(commit=False)

        user.set_password(form['password'])
        # save user with hashed password
        form.save()
        login(self.request, user)
        return redirect('store:index')


class UserLoginView(LoginView):
    def __init__(self, *args, **kwargs):
        super(UserLoginView, self).__init__(*args, **kwargs)

    authentication_form = UserLogin
    template_name = 'auth/singin.html'

    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            return redirect('store:index')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(user=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
