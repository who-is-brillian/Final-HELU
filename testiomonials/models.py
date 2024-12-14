from django.db import models

# Pilihan nama kelas
CLASS_CHOICES = [
    ('TOEFL Preparation', 'TOEFL Preparation'),
    ('Class Grammar', 'Class Grammar'),
    ('Class Reading', 'Class Reading'),
    ('Class Listening', 'Class Listening'),
    ('IELTS Preparation', 'IELTS Preparation'),
    ('Class Writing', 'Class Writing'),
    ('Class Speaking', 'Class Speaking'),
    ('Business English', 'Business English'),
]

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)  # Rating antara 1-5
    created_at = models.DateTimeField(auto_now_add=True)
    class_name = models.CharField(max_length=100, choices=CLASS_CHOICES, default='TOEFL Preparation')  # Menambahkan default

    def __str__(self):
        return f"Testimonial by {self.name} on {self.created_at}"
