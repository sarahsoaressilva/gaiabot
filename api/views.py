from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


# SIRENE
def view(request):
    return HttpResponse(status=200)
