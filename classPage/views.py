from django.shortcuts import render, get_object_or_404
from django.templatetags.static import static  # Import static
from .models import Classpages
from testiomonials.models import Testimonial
# Create your views here.


def class_page(request):
    classpages = Classpages.objects.all()

    context = {
        'title': 'Class Helu',
        'bannerClass': static('images/AboutUs.png'),
        'classes': classpages,
        }
    return render (request,'class.html', context)

def class_detail(request, url_slug):
    class_detail = get_object_or_404(Classpages, url_slug=url_slug)
    template_name = f'class_pages/{url_slug}.html'  # Gunakan nama template sesuai slug
    return render(request, template_name, {'class': class_detail})


def business(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'business.html', {'testimonials': testimonials})

def grammar(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'grammar.html', {'testimonials': testimonials})

def elts(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'elts.html', {'testimonials': testimonials})

def listening(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'listening.html', {'testimonials': testimonials})

def reading(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'reading.html', {'testimonials': testimonials})

def reading(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'reading.html', {'testimonials': testimonials})

def speaking(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'speaking.html', {'testimonials': testimonials})

def toefl(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'toefl.html', {'testimonials': testimonials})

def writing(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'writing.html', {'testimonials': testimonials})