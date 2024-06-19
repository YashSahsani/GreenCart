from functools import wraps
from django.shortcuts import redirect

def login_required(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        print(request.user)
        if not request.user.is_authenticated:
            # Redirect to login page if the user is not authenticated
            return redirect('Auth:login')
        return function(request, *args, **kwargs)
    return wrapper

def getSecondsOfOneYear():
    return 365 * 24 * 60 * 60 # 1 year in seconds


