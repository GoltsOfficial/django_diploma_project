import json
from json import JSONDecodeError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from backend.main.apps.auth_app.models import Record


@csrf_exempt
def sign_in(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode())
            user = authenticate(
                request,
                username = data.get('username'),
                password = data.get('password'),
            )
            if user is not None:
                login(request, user)
                return JsonResponse({'status': 'success'})
            return JsonResponse({f"Error": "Invalid credentials."}, status=401)
        except ImportError:
            return JsonResponse({"error", "Only POST allowed"}, status=405)

@csrf_exempt
def sing_up(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get('name')
            username = data.get('username')
            password = data.get('password')
            if not name or not username or not password:
                return JsonResponse({"error", "Need to fill all fields."}, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({"error", "Username already exists."}, status=400)

            user = User.objects.create_user(username=username, password=password)
            return JsonResponse({'status': 'signed_up', 'id': user.id}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error", "Invalid credentials."}, status=400)

    return JsonResponse({"error", "Only POST allowed."}, status=405)

@csrf_exempt
def sign_out(request):
    if request.method == "POST":
        try:
            logout(request)
            return JsonResponse({"status": "signed_out"}, status=200)

        except JSONDecodeError:
            return JsonResponse({"error", "Invalid JSON"}, status=400)

    return JsonResponse({"error", "Only POST allowed"}, status=405)

