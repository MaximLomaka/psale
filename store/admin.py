from django.contrib import admin

# Register your models here.
from store.models import Advertisement, Game

admin.site.register(Advertisement)
admin.site.register(Game)
