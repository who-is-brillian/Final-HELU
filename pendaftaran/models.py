from django.db import models
from django.contrib.auth.models import User

class Pendaftaran(models.Model):
    # Pilihan untuk kelas
    Kelas_Grammar = 'Kelas Grammar'
    Kelas_Listening = 'Kelas Listening'
    Kelas_Reading = 'Kelas Reading'
    Kelas_Writing = 'Kelas Writing'
    Kelas_Speaking = 'Kelas Speaking'
    Toefl_preparation = 'Toefl Preparation'
    ielts_preparation = 'Ielts Preparation'
    Business_English = 'Business English'

    KELAS_CHOICES = [
        (Kelas_Grammar, 'Kelas Grammar'),
        (Kelas_Listening, 'Kelas Listening'),
        (Kelas_Reading, 'Kelas Reading'),
        (Kelas_Writing, 'Kelas Writing'),
        (Kelas_Speaking, 'Kelas Speaking'),
        (Toefl_preparation, 'Toefl Preparation'),
        (ielts_preparation, 'Ielts Preparation'),
        (Business_English, 'Business English'),
    ]

    # Level class choices
    LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    # Pilihan untuk metode pembayaran
    TRANSFER = 'transfer'
    BCA = 'BCA'
    KREDIT = 'BRI'
    DEBIT = 'DANA'
    SHOPEEPAY = 'SHOPEEPAY'

    METODE_PEMBAYARAN_CHOICES = [
        (TRANSFER, 'Transfer'),
        (BCA, 'BCA'),
        (KREDIT, 'BRI'),
        (DEBIT, 'DANA'),
        (SHOPEEPAY, 'SHOPEEPAY'),
    ]

    # Status pembayaran
    PENDING = 'pending'
    LUNAS = 'Lunas'
    DITOLAK = 'ditolak'

    STATUS_PEMBAYARAN_CHOICES = [
        (PENDING, 'Pending'),
        (LUNAS, 'Lunas'),
        (DITOLAK, 'Ditolak'),
    ]

    # Field model
    kelas = models.CharField(
        max_length=255,
        choices=KELAS_CHOICES,
        default=Kelas_Grammar
    )

    level = models.CharField(
        max_length=255,
        choices=LEVEL_CHOICES,
        default='Beginner'
    )

    harga = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )

    nama = models.CharField(max_length=255)
    no_telpon = models.CharField(max_length=15, default="0000000000")
    email = models.EmailField(max_length=225, default="default@example.com")
    tanggal_pembayaran = models.DateField(auto_now_add=True)

    metode_pembayaran = models.CharField(
        max_length=255,
        choices=METODE_PEMBAYARAN_CHOICES
    )

    bukti_pembayaran = models.ImageField(upload_to='bukti_pembayaran/')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    status_pembayaran = models.CharField(
        max_length=20,
        choices=STATUS_PEMBAYARAN_CHOICES,
        default=PENDING
    )

    def __str__(self):
        return f'{self.nama} - {self.status_pembayaran}'