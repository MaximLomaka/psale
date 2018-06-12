from django.contrib.auth import views as auth_views
from django.urls import path

app_name = 'auth'
urlpatterns = [

    # path('', AdListView.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
]
