from django.urls import path

from store.views import AdListView

app_name = 'store'
urlpatterns = [

    path('', AdListView.as_view(), name='index'),
]
