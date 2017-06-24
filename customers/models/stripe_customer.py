from django.conf import settings
from django.db import models

class StripeCustomer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.stripe_id:
            return str(self.stripe_id)
        else:
            return str(self.user.username)

    def __unicode__(self):
        return self.__str__()
