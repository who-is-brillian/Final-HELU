from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Course, Material
from testiomonials.models import Testimonial
from django.core.paginator import Paginator


# View untuk halaman utama kursus dengan proteksi akses
@login_required
def course_page(request):
    if not request.user.lmspermission.is_allowed:
        return HttpResponseForbidden("You do not have permission to access the LMS.")
    
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

@login_required
def course_list(request):
    courses = Course.objects.all()
    paginator = Paginator(courses, 9)  # 10 kursus per halaman
    page_number = request.GET.get('page')
    page_courses = paginator.get_page(page_number)

    return render(request, 'courses/course_list.html', {'courses': page_courses})



# View untuk detail kursus berdasarkan ID
@login_required
def course_detail(request, course_id):
    if not request.user.lmspermission.is_allowed:
        return HttpResponseForbidden("You do not have permission to access the LMS.")
    
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

# View untuk halaman writing dengan menampilkan testimonials
@login_required
def writing(request):
    if not request.user.lmspermission.is_allowed:
        return HttpResponseForbidden("You do not have permission to access the LMS.")
    
    testimonials = Testimonial.objects.all()
    return render(request, 'courses/writing.html', {'testimonials': testimonials})


def course_detail(request, course_id):
    # Ambil data kursus berdasarkan course_id
    course = get_object_or_404(Course, id=course_id)

    # Ambil materi yang terkait dengan kursus tersebut
    materials = Material.objects.filter(course=course)

    # Render template dengan data kursus dan materi
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'materials': materials
    })