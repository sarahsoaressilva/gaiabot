from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def chat_view(request):
    return render(request, 'chat.html')