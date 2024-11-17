from django.db import models

# Create your models here.

class Classpages(models.Model):
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Standart'
    ADVANCED = 'Advanced'

    LEVEL_CHOICES = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Standart'),
        (ADVANCED, 'Advanced'),
    ]
    
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    start_date = models.DateField()
    duration = models.IntegerField()  # Durasi dalam bulan
    sessions = models.IntegerField()  # Jumlah pertemuan
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES, default=BEGINNER)
    image_url = models.CharField(max_length=255)

    link_page = models.CharField(max_length=200)

    def __str__(self):
        return self.title