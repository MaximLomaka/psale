from django.contrib.auth import views as auth_views
from django.urls import path

from store.views import *

app_name = 'store'
urlpatterns = [

    path('', AdListView.as_view(), name='index'),
    path('<int:pk>/', AdDetailView.as_view(), name='detail'),
    path('registration/', CreateUserView.as_view(), name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html')),
]
