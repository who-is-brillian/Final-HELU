# forms.py
from django import forms
from .models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone_number', 'email', 'username', 'profile_picture', 'address']
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }
