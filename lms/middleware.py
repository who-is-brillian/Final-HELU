from django.http import HttpResponseForbidden
from django.shortcuts import redirect

class LMSPermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Lewatkan permintaan ke admin panel tanpa pemeriksaan
        if request.path.startswith('/admin/'):
            return self.get_response(request)

        # Periksa apakah URL yang diakses adalah bagian dari LMS
        if '/lms/' in request.path:  # Atau sesuaikan dengan pola URL LMS Anda
            # Periksa apakah pengguna telah login
            if request.user.is_authenticated:
                # Periksa apakah pengguna memiliki LMSPermission
                if not hasattr(request.user, 'lmspermission') or not request.user.lmspermission.is_allowed:
                    # Jika tidak memiliki izin LMS, batalkan akses dan beri respons Forbidden
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
