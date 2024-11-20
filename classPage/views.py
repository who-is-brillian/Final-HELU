from django.shortcuts import render, get_object_or_404
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

def class_detail(request, url_slug):
    class_detail = get_object_or_404(Classpages, url_slug=url_slug)
    template_name = f'class_pages/{url_slug}.html'  # Gunakan nama template sesuai slug
    return render(request, template_name, {'class': class_detail})