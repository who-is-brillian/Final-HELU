from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'email', 'comment']
        widgets = {
        'name': forms.TextInput(attrs={'class': "w-100 form-control py-3 mb-3 border-primary", 'placeholder': 'Your Name'}),
        'email': forms.EmailInput(attrs={'class': "w-100 form-control py-3 mb-3 border-primary", 'placeholder': 'Your Email'}),
        'comment': forms.Textarea(attrs={'class': "w-100 form-control mb-3 border-primary", 'placeholder': 'Your Message'}),
        
    }
