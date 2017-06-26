from django.conf import settings
from django.db import models
from .customer import Customer

class StripeCustomer(models.Model):
    customer = models.OneToOneField(Customer)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        if self.stripe_id:
            return str(self.stripe_id)
        else:
            return str(self.user.username)

    def __unicode__(self):
        return self.__str__()
