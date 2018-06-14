from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.urls import path, include

from auth.views import UserSignUpView, UserLoginView

app_name = 'auth'
urlpatterns = [

    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),

]
