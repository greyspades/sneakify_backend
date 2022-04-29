from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('ludex gundyr')

def boots(request):
    return HttpResponse('semper fidelis')

def user(request, id):
    return HttpResponse('the name is ' % id)