from django.urls import path

from store.views import *

app_name = 'store'
urlpatterns = [

    path('', AdListView.as_view(), name='index'),
    path('<int:pk>/', AdDetailView.as_view(), name='detail'),
    path('user/<int:pk>/', GetMonetView.as_view(), name='user_detail'),
]
