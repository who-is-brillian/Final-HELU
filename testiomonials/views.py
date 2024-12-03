
from django.shortcuts import render, redirect
from .models import Testimonial
from .forms import TestimonialForm

def comments(request):
    # Ambil semua testimonial yang ada
    testimonials = Testimonial.objects.all()

    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            # Simpan data komentar ke database
            form.save()
            return redirect('other_Page')  # Redirect ke halaman index setelah submit
    else:
        form = TestimonialForm()

    return render(request, 'other_page.html', {'form': form, 'testimonials': testimonials})

