from datetime import datetime

from django.contrib.auth.models import User
from django.db.models import Model, CharField, IntegerField, DateTimeField, ForeignKey, CASCADE, \
    ManyToManyField, OneToOneField


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
    coins = IntegerField(default=0)


class Game(Model):
    type = CharField(max_length=15)
    name = CharField(max_length=15)
    date_of_creation = DateTimeField(default=datetime.now())


# ad = ForeignKey(Advertisement, on_delete=CASCADE, related_query_name='games', related_name='game')
class Advertisement(Model):
    PLATFORMS = (
        ('PS4', 'PS4'),
        ('XBOX 1', 'XBOX 1'),
        ('PC', 'PC')
    )
    price = IntegerField()
    description = CharField(max_length=50, null=True)
    platform = CharField(max_length=20, choices=PLATFORMS)
    date_of_creation = DateTimeField(default=datetime.now())
    bid = IntegerField(null=True)
    user = ForeignKey(User, on_delete=CASCADE, related_name='ad', related_query_name='ads')
    games = ManyToManyField(Game, related_name='game', related_query_name='games')
