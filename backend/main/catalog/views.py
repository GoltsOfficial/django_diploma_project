from django.http import JsonResponse

def categories(request):
    return JsonResponse([], safe=False)

def catalog(request):
    return JsonResponse({"items": [], "currentPage": 1, "lastPage": 1})

def popular_products(request):
    return JsonResponse([], safe=False)

def limited_products(request):
    return JsonResponse([], safe=False)

def sales(request):
    return JsonResponse({"items": [], "currentPage": 1, "lastPage": 1})

def banners(request):
    return JsonResponse([], safe=False)