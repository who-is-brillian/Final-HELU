from django.db import models

# Create your models here.
class Count(models.Model):
    student_count = models.IntegerField()
    mentor_count = models.IntegerField()
    class_count = models.IntegerField()

    def __str__(self):
        # Gabungkan nilai menjadi satu string
        return f"Students: {self.student_count}, Mentors: {self.mentor_count}, Classes: {self.class_count}"

class Class(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    start_date = models.DateField()
    duration = models.IntegerField()  # Durasi dalam bulan
    sessions = models.IntegerField()  # Jumlah pertemuan
    level = models.CharField(max_length=50)
    image_url = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Mentor(models.Model):
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=150)
    linkYt = models.URLField(blank=True)
    linkIg = models.URLField()
    linkFb = models.URLField()
    image_mentor = models.CharField(max_length=200)                                                                                                                                                                                                                                                                                                                                                                                                 
    def __str__(self):
        return self.nama