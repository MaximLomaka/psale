'''forms for authentication'''
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.forms import CharField, PasswordInput, EmailField


class UserCreate(UserCreationForm):
    '''form for user registration'''
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
        return cleaned_data


class UserLogin(AuthenticationForm):
    '''form for log in user'''
    username = CharField(max_length=15)
    password = CharField(max_length=15,widget=PasswordInput())
