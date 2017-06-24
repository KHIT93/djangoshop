from django.db import models

class AppSetting(models.Model):
    key = models.CharField(max_length=255)
    value = models.TextField()

    def __str__(self):
        return str(self.key)

    def __unicode__(self):
        return self.__str__()
