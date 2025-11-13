from django.http import JsonResponse

def payment(request, id):
    return JsonResponse({'message': f'Payment for order id: {id}', 'app': 'payment'})

def payment_someone(request):
    return JsonResponse({'message': 'Payment someone endpoint', 'app': 'payment'})

def payment_progress(request):
    return JsonResponse({'message': 'Payment progress endpoint', 'app': 'payment'})
