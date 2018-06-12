from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from store.views import AdViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'ads', AdViewSet)
router.register(r'users', UserViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    url(r'api/', include(router.urls)),
    path(r'auth/', include('auth.urls'))
]
