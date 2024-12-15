from django.shortcuts import render, get_object_or_404
from .models import Course
from .decorators import lms_permission_required
from django.contrib.auth.decorators import login_required
from testiomonials.models import Testimonial 

# View untuk halaman utama course dengan proteksi akses
@login_required
@lms_permission_required
def course_page(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

# View untuk daftar semua course (tanpa proteksi, contoh umum)
@login_required
@lms_permission_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

# View untuk detail course berdasarkan ID
@login_required
@lms_permission_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

# View untuk halaman writing
@login_required
@lms_permission_required
def writing(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'courses/writing.html', {'testimonials': testimonials})
