from django.urls import path

from store.views import AdListView

urlpatterns = [

    path('', AdListView.as_view())
]
