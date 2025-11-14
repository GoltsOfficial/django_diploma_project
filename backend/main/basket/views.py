from django.http import JsonResponse

def basket(request):
    if request.method == 'GET':
        return JsonResponse([], safe=False)
    elif request.method == 'POST':
        return JsonResponse([], safe=False)
    elif request.method == 'DELETE':
        return JsonResponse([], safe=False)