from django.shortcuts import redirect

class RedirectInvalidURLsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:  # Jika halaman tidak ditemukan
            return redirect('/')  # Ubah ke URL target Anda
        return response
