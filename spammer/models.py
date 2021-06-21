from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from core.models import BaseAbstractModel


class Email(BaseAbstractModel):
    subject = models.CharField(max_length=255)
    text = models.TextField()
    email_to = models.EmailField()

    def __str__(self):
        return self.email_to
    
    def save(self, force_insert=False, force_update=False,
             using=None, update_fields=None):

        send_mail(
            self.subject, self.text, settings.EMAIL_HOST_USER,
            [self.email_to], True)
            
        return super().save(force_insert, force_update, using, update_fields)