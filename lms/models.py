from django.db import models

class Course(models.Model):
    LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.CharField(max_length=255)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    duration = models.IntegerField(help_text="Duration in hours")
    price = models.DecimalField(max_digits=10, decimal_places=3)
    image = models.ImageField(upload_to='courses/images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title