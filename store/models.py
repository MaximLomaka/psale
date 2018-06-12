from datetime import datetime

from django.db.models import Model, CharField, IntegerField, DateTimeField


class Advertisement(Model):
    price = IntegerField()
    description = CharField(max_length=50)
    platform = CharField(max_length=20)
    time_of_create = DateTimeField(default=datetime.now())
    bid = IntegerField()
