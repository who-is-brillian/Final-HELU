from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.templatetags.static import static  # Import static
from .models import Count,Class,Mentor
from testiomonials.models import Testimonial


def index(request):
    count = Count.objects.first()
    classes = Class.objects.all()
    mentors = Mentor.objects.all()

    # Gabungkan kedua konteks
    context = {
        'title': 'Home Helu',
        'banner1': static('images/Carousel.png'),
        'banner2': static('images/Carousel1.png'),
        'banner3': static('images/Carousel2.png'),
        'student_count': count.student_count if count else 0,  # Jika tidak ada data Count, set ke 0
        'mentor_count': count.mentor_count if count else 0,    # Jika tidak ada data Count, set ke 0
        'class_count': count.class_count if count else 0,      # Jika tidak ada data Count, set ke 0
        'classes': classes,  # Tambahkan classes ke dalam konteks
        'mentors': mentors,
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'title': 'About Helu',
        'bannerClass': static('images/AboutUs.png'),

        }
    return render (request,'about.html', context)

def homeTestimonial(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'index.html', {'testimonials': testimonials})