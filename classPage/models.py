from django.db import models

# Create your models here.

class Classpages(models.Model):
    # BEGINNER = 'Beginner'
    # INTERMEDIATE = 'Intermediate'
    # ADVANCED = 'Advanced'

    # LEVEL_CHOICES = [
    #     (BEGINNER, 'Beginner'),
    #     (INTERMEDIATE, 'Intermediate'),
    #     (ADVANCED, 'Advanced'),
    # ]
    
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    start_date = models.DateField()
    duration = models.IntegerField()  # Durasi dalam bulan
    sessions = models.IntegerField()  # Jumlah pertemuan
    level = models.CharField(max_length=50,)
    image_url = models.CharField(max_length=255)

    url_slug = models.CharField(max_length=50,)  # Default URL slug

    def __str__(self):
        return self.title