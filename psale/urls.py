from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from store.views import AdViewSet, UserViewSet

ROUTER = routers.DefaultRouter()
ROUTER.register(r'ads', AdViewSet)
ROUTER.register(r'users', UserViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    url(r'api/', include(ROUTER.urls)),
    path(r'accounts/', include('auth.urls')),
]
