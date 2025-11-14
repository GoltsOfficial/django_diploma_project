from django.http import JsonResponse

def orders(request):
    if request.method == 'GET':
        return JsonResponse([], safe=False)
    elif request.method == 'POST':
        return JsonResponse({"orderId": 123})

def order_detail(request, id):
    if request.method == 'GET':
        return JsonResponse({"id": id})
    elif request.method == 'POST':
        return JsonResponse({"id": id})