from django.dispatch import receiver
from django.db.models.signals import post_save

from accounts.models import Profile,User, Younger, Elder


@receiver(post_save,sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_elder:
            print(instance.is_elder)
            Profile.objects.create(user = instance, is_elder_profile = True)
        else:
            Profile.objects.create(user = instance, is_younger_profile = True)
