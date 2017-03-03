from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Subject(models.Model):

    #university = models.ForeignKey('university', on_delete=models.CASCADE)

    title = models.CharField(
        _('title'),
        max_length=255
    )

    ntnuCredits = models.DecimalField(
        _('ntnuCredits'),
        max_digits=5,
        decimal_places=2
    )


    description = models.TextField(
        _('description')
    )

    def __str__(self):
        return '{}'.format(self.title)
