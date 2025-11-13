from django.http import JsonResponse

def catalog_list(request):
    return JsonResponse({'message': 'Catalog list endpoint', 'app': 'catalog'})

def catalog_detail(request, id):
    return JsonResponse({'message': f'Catalog detail for id: {id}', 'app': 'catalog'})

def categories(request):
    return JsonResponse({'message': 'Categories endpoint', 'app': 'catalog'})

def sale_products(request):
    return JsonResponse({'message': 'Sale products endpoint', 'app': 'catalog'})
