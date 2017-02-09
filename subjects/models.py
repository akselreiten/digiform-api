from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Subject(models.Model):
    title = models.CharField(
        _('title'),
        max_length=255
    )

    description = models.TextField(
        _('description')
    )

    def __str__(self):
        return '{}'.format(self.title)
