'''urls for store'''
from django.contrib.auth.decorators import login_required
from django.urls import path

from store.views import AdListView, MoneyUpdateView, CreateAd, AdDetailView

app_name = 'store'
urlpatterns = [

    path('', login_required(AdListView.as_view()), name='index'),

    path('<int:pk>/', login_required(MoneyUpdateView.as_view()), name='money_detail'),
    path('accounts/<int:pk>/ad/', login_required(CreateAd.as_view()), name='create_ad'),
    path('ad/<int:pk>/', login_required(AdDetailView.as_view()), name='detail'),

]
