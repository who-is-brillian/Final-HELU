from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    # Menambahkan konfirmasi password untuk validasi
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    # Validasi untuk memastikan password dan konfirmasi password cocok
    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password and Confirm Password do not match")
        return password2
