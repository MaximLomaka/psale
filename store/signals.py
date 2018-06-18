'''signals for store'''
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from store.models import Money


@receiver(post_save, sender=User)
def user_create_signal(sender, instance, created, **kwargs):
    '''creating money model when new user appears '''
    if created:
        Money.objects.create(user=instance, coins=0)
