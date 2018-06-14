from django.urls import path

from store.views import *

app_name = 'store'
urlpatterns = [

    path('', login_required(AdListView.as_view()), name='index'),
    path('<int:pk>/', login_required(AdDetailView.as_view()), name='detail'),
    path('user/<int:pk>/', login_required(GetMonetView.as_view()), name='user_detail'),
]
