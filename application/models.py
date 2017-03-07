from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class Application(models.Model):

    user = models.ForeignKey(User,
                             verbose_name="user",
                             on_delete=models.CASCADE)

    ntnuSubject = models.ForeignKey('subjects.Subject', related_name="ntnuSubject",
                                    verbose_name="NTNU subject",
                                    on_delete=models.CASCADE)
    replacingSubject = models.ForeignKey('subjects.Subject', related_name ="replacingSubject",
                                         verbose_name ="replacing subject",
                                         on_delete=models.CASCADE)


    justification = models.TextField(
        _('justification')
    )

    def __str__(self):
        return '{}'.format(self.user)