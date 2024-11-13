from django import forms
from .models import Mailbox
from django_recaptcha.fields import ReCaptchaField

    

class MailboxForm(forms.ModelForm):
    captcha = ReCaptchaField(label='')

    class Meta:
        model = Mailbox
        fields =["mail_name", "mail_email", "mail_message", "captcha"]
        widgets = {
            'mail_name': forms.TextInput(attrs={'class': "w-100 form-control py-3 mb-3 border-primary", 'placeholder': 'Your Name'}),
            'mail_email': forms.EmailInput(attrs={'class': "w-100 form-control py-3 mb-3 border-primary", 'placeholder': 'Your Email'}),
            'mail_message': forms.Textarea(attrs={'class': "w-100 form-control mb-3 border-primary", 'placeholder': 'Your Message'}),
            
        }
        labels = {
            'mail_name': '',
            'mail_email': '',
            'mail_message': '',
            
            
        }