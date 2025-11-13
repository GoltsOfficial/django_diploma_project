from django.http import JsonResponse

def product_detail(request, id):
    return JsonResponse({'message': f'Product detail id: {id}', 'app': 'product'})

def product_search(request):
    return JsonResponse({'message': 'Product search endpoint', 'app': 'product'})

def popular_products(request):
    return JsonResponse({'message': 'Popular products endpoint', 'app': 'product'})
