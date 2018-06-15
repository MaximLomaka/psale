from django.urls import path

from store.views import *

app_name = 'store'
urlpatterns = [

    path('', login_required(AdListView.as_view()), name='index'),

    path('<int:pk>/', login_required(MoneyDetailView.as_view()), name='money_detail'),
    path('accounts/<int:pk>/ad/', login_required(CreateAd.as_view()), name='create_ad'),
    # path('<int:pk>/', login_required(AdDetailView.as_view()), name='detail'),
]
