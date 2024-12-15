from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import resolve
from lms.models import Course

class LMSPermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Lewatkan permintaan ke admin panel tanpa pemeriksaan
        if request.path.startswith('/admin/'):
            return self.get_response(request)

        # Periksa apakah URL yang diakses adalah bagian dari LMS
        if '/lms/' in request.path:  # Sesuaikan dengan pola URL LMS Anda
            # Periksa apakah pengguna telah login
            if request.user.is_authenticated:
                # Periksa apakah pengguna memiliki LMSPermission
                lms_permission = getattr(request.user, 'lmspermission', None)
                if lms_permission and lms_permission.is_allowed:
                    # Gunakan resolve untuk mendapatkan course_id dari URL
                    resolver_match = resolve(request.path)
                    course_id = resolver_match.kwargs.get('course_id')  # Mengambil course_id dari URL
                    try:
                        course = Course.objects.get(id=course_id)
                        # Periksa apakah kursus yang diakses ada dalam izin pengguna
                        if course not in lms_permission.courses.all():
                            return HttpResponseForbidden(
                                """
                                You do not have permission to access this course.
                                <br>
                                <a href="/courses/page/">Go back to the homepage</a>
                                """
                            )
                    except Course.DoesNotExist:
                        return HttpResponseForbidden(
                            """
                            Course not found.
                            <br>
                            <a href="/courses/page/">Go back to the homepage</a>
                            """
                        )
                else:
                    return HttpResponseForbidden(
                        """
                        You do not have permission to access the LMS.
                        <br>
                        <a href="/">Go back to the homepage</a>
                        """
                    )
            else:
                # Jika pengguna belum login, arahkan ke halaman login
                return redirect('login')  # Redirect ke URL login di proyek utama

        # Lanjutkan proses request jika semua pemeriksaan lolos (untuk halaman selain LMS)
        return self.get_response(request)
