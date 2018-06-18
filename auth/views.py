'''views for authentication'''
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views.generic import CreateView, ListView, TemplateView
from auth.email import check_user_by_email
from auth.forms import UserCreate
from auth.forms import UserLogin
from auth.tokens import account_activation_token
from store.models import Advertisement


class UserSignUpView(CreateView):
    '''regestration new user'''
    model = User
    form_class = UserCreate
    template_name = 'auth/sign_up.html'

    def form_invalid(self, form):
        return redirect('auth:signup')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.email = form.cleaned_data.get('email')
        user.save()
        current_site = get_current_site(self.request)
        check_user_by_email(user, user.email, current_site)

        return redirect('auth:login')


class UserDetailView(ListView):
    queryset = Advertisement.objects.all().filter()
    template_name = 'auth/user-detail.html'

    def get_queryset(self):
        pass


class UserSigninView(LoginView):
    '''login view'''
    authentication_form = UserLogin
    template_name = 'auth/login.html'

    def form_valid(self, form):
        '''when form is valid we authenticate user '''
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(user=username, password=password)

        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class ActivateUserView(TemplateView):

    def get(self, request, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(kwargs['uidb64']))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError):
            user = None
        if user is not None and account_activation_token.check_token(user, kwargs['token']):
            user.is_active = True
            user.save()
            login(request, user)
            return render(self.request, 'auth/activation_info.html',
                          context={'message': 'Thank you for your email confirmation.'
                                              ' Now you can login your account.'})
        else:
            return render(self.request, 'auth/activation_info.html',
                          context={'message': 'Activation link is invalid!'})
