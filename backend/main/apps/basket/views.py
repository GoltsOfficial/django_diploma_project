from django.http import JsonResponse

def basket_view(request):
    return JsonResponse({'message': 'Basket view endpoint', 'app': 'basket'})

def add_to_basket(request):
    return JsonResponse({'message': 'Add to basket endpoint', 'app': 'basket'})

def remove_from_basket(request, id):
    return JsonResponse({'message': f'Remove from basket id: {id}', 'app': 'basket'})

def update_basket(request, id):
    return JsonResponse({'message': f'Update basket id: {id}', 'app': 'basket'})
