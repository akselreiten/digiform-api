from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField(
        _('text')
    )

    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        message = '{}'.format(self.time_stamp) + "| "
        message += '{}'.format(self.sender)
        message += ": " + '{}'.format(self.text)
        return message

    def __unicode__(self):
        return u'%s' %(self.text)

