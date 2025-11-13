from django.http import JsonResponse

def sign_in(request):
    return JsonResponse({'message': 'Sign in endpoint', 'app': 'auth_app'})

def sign_up(request):
    return JsonResponse({'message': 'Sign up endpoint', 'app': 'auth_app'})

def logout_view(request):
    return JsonResponse({'message': 'Logout endpoint', 'app': 'auth_app'})

def profile(request):
    return JsonResponse({'message': 'Profile endpoint', 'app': 'auth_app'})