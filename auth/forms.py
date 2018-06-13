from django.contrib.auth.models import User

from django.forms import ModelForm, CharField, PasswordInput


class UserCreate(ModelForm):
    confirm_password = CharField(max_length=20, widget=PasswordInput())

    class Meta:
        model = User

        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def clean(self):
        cleaned_data = super(UserCreate, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data


class UserLogin(ModelForm):
    class Meta:
        model = User

        fields = ('username', 'password',)
