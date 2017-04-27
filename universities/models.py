from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class University(models.Model):

    #university name
    title = models.CharField(
        _('title'),
        max_length=255
    )

    #unviersity country
    country = models.CharField(
        _('country'),
        max_length=255
    )

    #university city
    city = models.CharField(
        _('city'),
        max_length=255
    )

    #univeristy description
    description = models.TextField(
        _('description')
    )

    #to-string method
    def __str__(self):
        return '{}'.format(self.title)