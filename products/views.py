from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def products(request):
    return JsonResponse({'message': 'Hello, World!'})
