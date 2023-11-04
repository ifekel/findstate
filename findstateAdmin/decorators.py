from functools import wraps
from django.shortcuts import redirect, reverse

def admin_only(redirect_url):
    def decorator(f):
        @wraps(f)
        def _wrapper(request, *args, **kwargs):
            if request.user.is_authenticated and not request.user.is_superuser:
                return redirect(reverse(redirect_url))
            return f(request, *args, **kwargs)
        return _wrapper
    return decorator


def prevent_authorized_access(f):
    @wraps(f)
    def _wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('admin:dashboard'))
        
        return f(request, *args, **kwargs)
    return _wrapper