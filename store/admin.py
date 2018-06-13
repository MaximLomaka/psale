from django.contrib import admin

# Register your models here.
from store.models import Advertisement, Game, Money

admin.site.register(Advertisement)
admin.site.register(Game)
admin.site.register(Money)
