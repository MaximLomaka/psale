'''serializers for store'''
from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer

from store.models import Advertisement


class UserSerializer(HyperlinkedModelSerializer):
    '''serializer for user'''

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'username', ]


class AdSerializer(HyperlinkedModelSerializer):
    '''serializer for advertisement'''

    class Meta:
        model = Advertisement
        exclude = ('date_of_creation', 'bid')
