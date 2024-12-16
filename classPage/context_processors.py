from testiomonials.models import Testimonial

def global_testimonials(request):
    return {
        'global_testimonials': Testimonial.objects.all()
    }