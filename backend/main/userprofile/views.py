from django.http import JsonResponse

def profile(request):
    if request.method == 'GET':
        return JsonResponse({"fullName": "User", "email": "user@mail.ru"})
    elif request.method == 'POST':
        return JsonResponse({"fullName": "User", "email": "user@mail.ru"})

def profile_password(request):
    return JsonResponse({"status": "success"})

def profile_avatar(request):
    return JsonResponse({"src": "/avatar.png", "alt": "Avatar"})