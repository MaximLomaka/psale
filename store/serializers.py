from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer

from store.models import Advertisement


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'username', ]


class AdSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Advertisement
        exclude = ('time_of_create',)
