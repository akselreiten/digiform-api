from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.
class Application(models.Model):

    STATUS_PROCESSING = "Processing"
    STATUS_ACCEPTED = "Accepted"
    STATUS_DECLINED = "Declined"

    STATUS_CHOICES = (
        (STATUS_PROCESSING, _('Processing')),
        (STATUS_ACCEPTED, _('Accepted')),
        (STATUS_DECLINED, _('Declined'))
    )


    user = models.ForeignKey(User,
                             verbose_name="user",
                             on_delete=models.CASCADE)

    ntnu_subject = models.ForeignKey('subjects.Subject', related_name="ntnuSubject",
                                     verbose_name="NTNU subject",
                                     on_delete=models.CASCADE)

    replacing_subject = models.ForeignKey('subjects.Subject', related_name="replacingSubject",
                                          verbose_name="replacing subject",
                                          on_delete=models.CASCADE)

    justification = models.TextField(
        _('justification')
    )

    application_status = models.CharField(
        choices=STATUS_CHOICES,
        default=STATUS_PROCESSING,
        max_length=20
    )

    def __str__(self):
        return '{}'.format(self.user)
