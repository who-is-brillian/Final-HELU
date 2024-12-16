from django import forms
from .models import Pendaftaran

class PendaftaranForm(forms.ModelForm):
    class Meta:
        model = Pendaftaran
        fields = ['kelas', 'level', 'harga', 'nama', 'no_telpon', 'metode_pembayaran', 'bukti_pembayaran']
        widgets = {
            'harga': forms.NumberInput(attrs={'readonly': 'readonly', 'class': 'form-control custom-class'}),
            'kelas': forms.Select(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'no_telpon': forms.TextInput(attrs={'class': 'form-control'}),
            'metode_pembayaran': forms.Select(attrs={'class': 'form-control'}),
            'bukti_pembayaran': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Tidak perlu lagi update harga di sini karena sudah diatur di `widgets`
        # Jika Anda ingin menambahkan pengaturan khusus lainnya pada field lain, bisa dilakukan di sini
