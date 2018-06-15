from datetime import datetime

from django.contrib.auth.models import User
from django.db.models import Model, CharField, IntegerField, DateTimeField, ForeignKey, CASCADE, \
    ManyToManyField, OneToOneField, PositiveIntegerField, DecimalField


# class User(Model):
#     first_name = CharField(max_length=20)
#     last_name = CharField(max_length=20)
#     email = EmailField(max_length=30, unique=True)
#     password = CharField(max_length=20, )
#     username = CharField(max_length=20, unique=True)
#     money = IntegerField(null=True)
#     date_of_creation = DateTimeField(default=datetime.now())
#
#     def __str__(self):
#         return self.first_name + ' ' + self.last_name
class Money(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_query_name='moneys', related_name='money')
    coins = PositiveIntegerField(default=0)


class Game(Model):
    type = CharField(max_length=15)
    name = CharField(max_length=15)
    date_of_creation = DateTimeField(default=datetime.now())


class Advertisement(Model):
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
    user = ForeignKey(User, on_delete=CASCADE, related_name='ad', related_query_name='ads', null=True)
    games = ForeignKey(Game, related_name='game', related_query_name='games', on_delete=CASCADE, default=None,
                       null=True)
