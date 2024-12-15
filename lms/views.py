from django.shortcuts import render, get_object_or_404
from .models import Course
from testiomonials.models import Testimonial  # Perbaikan typo pada "testimonials"
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# View untuk halaman utama course dengan proteksi akses
@login_required
def course_page(request):
    # Periksa apakah pengguna memiliki izin melalui LMSPermission
    if not hasattr(request.user, 'lmspermission') or not request.user.lmspermission.is_allowed:
        return HttpResponseForbidden("You do not have permission to access this page.")
    # Jika diizinkan, render halaman course list
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

# View untuk daftar semua course (tanpa proteksi)
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

# View untuk detail course berdasarkan ID
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

# View untuk halaman writing dengan menampilkan testimonials
def writing(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'courses/writing.html', {'testimonials': testimonials})
