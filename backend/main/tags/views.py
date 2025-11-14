from django.http import JsonResponse

def tags(request):
    return JsonResponse([], safe=False)