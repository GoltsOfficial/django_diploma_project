from django.http import JsonResponse

def payment(request):
    return JsonResponse({"status": "success"})