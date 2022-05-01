from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import requests

# Create your views here.

def index(request):
    return HttpResponse('ludex gundyr')

def boots(request):
    return HttpResponse('semper fidelis')

def user(request, id):
    return HttpResponse('the name is ' % id)

def get_sneakers(request):
    url = "https://v1-sneakers.p.rapidapi.com/v1/sneakers"
    querystring = {"limit":"10"}
    headers = {
	"X-RapidAPI-Host": "v1-sneakers.p.rapidapi.com",
	"X-RapidAPI-Key": "a9c9774493mshf4df80a9e398926p1ffb86jsn33ae009aa91c"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    #print(response.text)
    #return JsonResponse(response)
    return HttpResponse(response)