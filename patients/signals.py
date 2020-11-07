from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from patients.models import Profile, AuthorizedParties, Consent

# from users.models import Profile
@receiver(pre_save, sender=User)
def log_user(sender, instance, update_fields, **kwargs):
    AuthorizedParties.objects.create()


#     if created:
#         Profile.objects.create(user=instance)
#     else:
#         instance.profile.save()
