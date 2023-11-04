from functools import wraps
from django.shortcuts import redirect, reverse

def admin_only(f):
    @wraps(f)
    def _wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('admin:login'))
        if not request.user.is_superuser:
            return redirect(reverse('app:home'))
        return f(request, *args, **kwargs)
    return _wrapper


def prevent_authorized_access(f):
    @wraps(f)
    def _wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('admin:dashboard'))
        
        return f(request, *args, **kwargs)
    return _wrapper