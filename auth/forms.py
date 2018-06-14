from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm, CharField, PasswordInput, EmailField


class UserCreate(UserCreationForm):
    username = CharField(max_length=15)
    email = EmailField(max_length=24)
    password = CharField(max_length=20, widget=PasswordInput())
    confirm_password = CharField(max_length=20, widget=PasswordInput())

    def clean(self):
        cleaned_data = super(UserCreate, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data


class UserLogin(AuthenticationForm):
    username = CharField(max_length=15)
    password = CharField(max_length=15)
