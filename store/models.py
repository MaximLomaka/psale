'''main models '''
from datetime import datetime

from django.contrib.auth.models import User
from django.db.models import Model, CharField, DateTimeField, ForeignKey, CASCADE, \
    OneToOneField, PositiveIntegerField, DecimalField


class Money(Model):
    '''additional field for user'''
    user = OneToOneField(User, on_delete=CASCADE, related_query_name='moneys', related_name='money')
    coins = PositiveIntegerField(default=0)


class Game(Model):
    '''game field for advertisement '''
    type = CharField(max_length=15)
    name = CharField(max_length=15)
    date_of_creation = DateTimeField(default=datetime.now())


class Advertisement(Model):
    '''advertisement'''
    PLATFORMS = (
        ('steam', 'steam'),
        ('origin ', 'origin '),
        ('uplay', 'uplay'),
        ('battlenet', 'battlenet'),
    )
    price = DecimalField(null=True, max_digits=6, decimal_places=2)
    description = CharField(max_length=50, null=True)
    platform = CharField(max_length=20, choices=PLATFORMS, null=True)
    date_of_creation = DateTimeField(default=datetime.now(), null=True)
    bid = PositiveIntegerField(null=True)
    user = ForeignKey(User, on_delete=CASCADE, related_name='ad',
                      related_query_name='ads', null=True)
    games = ForeignKey(Game, related_name='game', related_query_name='games',
                       on_delete=CASCADE, default=None, null=True)
