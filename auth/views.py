# Create your views here.
import token

from django.core.mail import EmailMessage

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView, TemplateView

from auth.forms import UserCreate, UserLogin
from auth.tokens import account_activation_token


class UserSignUpView(CreateView):
    model = User
    form_class = UserCreate
    template_name = 'auth/sign_up.html'

    def form_invalid(self, form):

        return redirect('auth:signup')

    def form_valid(self, form):
        print('dfsfsfas')
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'Activate your account'
        message = render_to_string('auth/active_email.html',
                                   {
                                       'user': user,
                                       'domain': current_site.domain,
                                       'uid': str(urlsafe_base64_encode(force_bytes(user.pk)), encoding='utf-8'),
                                       'token': account_activation_token.make_token(user),
                                   })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()

        # user.set_password(form['password'])
        # save user with hashed password
        # form.save()

        # login(self.request, user)

        return redirect('auth:login')


class UserLoginView(LoginView):
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
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, kwargs['token']):
            user.is_active = True
            user.save()
            login(request, user)
            # return redirect('home')
            return render(self.request, 'auth/activation_info.html',
                          context={'message': 'Thank you for your email confirmation. Now you can login your account.'})
        else:
            return render(self.request, 'auth/activation_info.html',
                          context={'message': 'Activation link is invalid!'})
