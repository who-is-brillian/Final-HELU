from django import forms
from django.contrib.auth.models import User
from user.models import UserProfileInfo
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class UserForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
            'maxlength': '150',
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password',
        }), 
        label="Confirm Password"
    )

    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).last()

        if password and confirm_password and password != confirm_password:
            # raise forms.ValidationError("Password and Confirm Password do not match.")
            self.add_error('password','Password and Confirm Password do not match.')
        if user:
            # raise forms.ValidationError("email yang sudah anda masukan sudah terdaftar!")    
            self.add_error('email',"email yang sudah anda masukan sudah terdaftar!")
        return cleaned_data

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    portfolio_site = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your portfolio URL (optional)',
        })
    )
    profile_pic = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file',
        })
    )

    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
