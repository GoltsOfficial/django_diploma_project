from django.http import JsonResponse

def tags_list(request):
    return JsonResponse({'message': 'Tags list endpoint', 'app': 'tags'})

def tag_products(request, id):
    return JsonResponse({'message': f'Tag products for tag id: {id}', 'app': 'tags'})
