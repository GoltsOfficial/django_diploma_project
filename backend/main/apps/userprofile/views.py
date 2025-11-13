from django.http import JsonResponse

def profile_view(request):
    return JsonResponse({'message': 'Profile view endpoint', 'app': 'userprofile'})

def update_profile(request):
    return JsonResponse({'message': 'Update profile endpoint', 'app': 'userprofile'})

def account_settings(request):
    return JsonResponse({'message': 'Account settings endpoint', 'app': 'userprofile'})

def order_history(request):
    return JsonResponse({'message': 'Order history endpoint', 'app': 'userprofile'})
