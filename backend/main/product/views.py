from django.http import JsonResponse

def product_detail(request, id):
    return JsonResponse({"id": id, "title": "Product"})

def product_review(request, id):
    return JsonResponse([], safe=False)