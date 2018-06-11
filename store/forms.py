from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, PasswordInput


class UserForm(ModelForm):
    password = CharField(widget=PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'username', ]
