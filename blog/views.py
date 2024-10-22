from django.shortcuts import render
from django.Http import HttpResponse

# Create your views here.

def my_blog(request):
    retutn HttpResponse("Hello, Blog!")