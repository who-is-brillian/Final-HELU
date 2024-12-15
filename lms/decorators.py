from django.http import HttpResponseForbidden
from functools import wraps

def lms_permission_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Periksa apakah pengguna memiliki LMSPermission
        if not hasattr(request.user, 'lmspermission') or not request.user.lmspermission.is_allowed:
            return HttpResponseForbidden(
                        """
                        You do not have permission to access this page.
                        <br>
                        <a href="/">Go back to the homepage</a>
                        """
                                         )
        return view_func(request, *args, **kwargs)
    return _wrapped_view
