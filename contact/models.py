from django.db import models

# Create your models here.
class Mailbox(models.Model):
    mail_name = models.CharField(max_length=100, blank=False, null=False)
    mail_email = models.EmailField( blank=False, null=False)
    mail_message = models.CharField( max_length=500, blank=False, null=False)


    def __str__(self):
        return self.mail_name