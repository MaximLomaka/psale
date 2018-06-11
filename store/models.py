from django.db.models import Model, CharField, IntegerField


class Advertisement(Model):
    price = IntegerField()
    description = CharField(max_length=50)
    platform = CharField(max_length=20)
