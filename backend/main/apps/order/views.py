from django.http import JsonResponse

def order_list(request):
    return JsonResponse({'message': 'Order list endpoint', 'app': 'order'})

def order_detail(request, id):
    return JsonResponse({'message': f'Order detail id: {id}', 'app': 'order'})

def create_order(request):
    return JsonResponse({'message': 'Create order endpoint', 'app': 'order'})

def order_history(request):
    return JsonResponse({'message': 'Order history endpoint', 'app': 'order'})
