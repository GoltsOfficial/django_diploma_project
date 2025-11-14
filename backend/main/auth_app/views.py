from django.http import JsonResponse

def sign_in(request):
    return JsonResponse({'message': 'Sign in endpoint'})

def sign_up(request):
    return JsonResponse({'message': 'Sign up endpoint'})

def sign_out(request):
    return JsonResponse({'message': 'Sign out endpoint'})