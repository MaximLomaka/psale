from django.contrib.auth.models import User
from django.forms import ModelForm


class UserCreate(ModelForm):
    class Meta:
        model = User

        fields = ('username', 'password', 'first_name', 'last_name', 'email')
