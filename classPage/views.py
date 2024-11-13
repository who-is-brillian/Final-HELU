from django.shortcuts import render
from django.shortcuts import render
from django.templatetags.static import static  # Import static
from .models import Classpages

# Create your views here.


def class_page(request):
    classpages = Classpages.objects.all()

    context = {
        'title': 'Class Helu',
        'bannerClass': static('images/AboutUs.png'),
        'classes': classpages,
        }
    return render (request,'class.html', context)