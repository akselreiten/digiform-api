from django.db import models
from django.utils.translation import ugettext_lazy as _



# Create your models here.
class Subject(models.Model):

    #university lecturing the subject
    university = models.ForeignKey("universities.University", on_delete=models.CASCADE)

    #subject title
    title = models.CharField(
        _('title'),
        max_length=255
    )

    #course code of subject
    courseCode = models.CharField(
        "course code",
        max_length=20)

    #number of NTNU credits the subject provides
    ntnuCredits = models.DecimalField(
        _('ntnuCredits'),
        max_digits=4,
        decimal_places=2
    )

    #subject description
    description = models.TextField(
        _('description'),
        blank = True
    )

    #to-string method
    def __str__(self):
        return '{}'.format(self.title)

