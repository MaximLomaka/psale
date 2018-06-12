from django.contrib.auth import views as auth_views
from django.urls import path

from auth.views import UserSignUpView

app_name = 'auth'
urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),

]
