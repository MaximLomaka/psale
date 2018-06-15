from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm, CharField, PasswordInput, EmailField


class UserCreate(UserCreationForm):
    username = CharField(max_length=15)
    email = EmailField(max_length=24)
    password1 = CharField(max_length=20, widget=PasswordInput())
    password2 = CharField(max_length=20, widget=PasswordInput())

    def clean(self):
        '''check passwords validation'''
        cleaned_data = super(UserCreate, self).clean()

        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")

        if password != confirm_password:
            self.add_error('password2', "Password does not match")
        elif password is None:
            self.add_error('password1', 'Password can not be empty')
        elif password.__len__ < 8:
            self.add_error('password1', 'Password length must be greater then 8')
        return cleaned_data


class UserLogin(AuthenticationForm):
    username = CharField(max_length=15)
    password = CharField(max_length=15)
