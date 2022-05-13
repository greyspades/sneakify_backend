from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from sneakers.models import User
import json
from django.core import serializers

method_decorator(csrf_protect)

@csrf_exempt
# @api_view(['POST'])

# Create your views here.

def index(request):
    return HttpResponse('ludex gundyr')

def boots(request):
    return HttpResponse('semper fidelis')

# def user(request, id):
#     return HttpResponse('the name is ' % id)

def get_sneakers(request):
    url = "https://v1-sneakers.p.rapidapi.com/v1/sneakers"
    querystring = {"limit":"12"}
    headers = {
	"X-RapidAPI-Host": "v1-sneakers.p.rapidapi.com",
	"X-RapidAPI-Key": "a9c9774493mshf4df80a9e398926p1ffb86jsn33ae009aa91c"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)
    #return JsonResponse(response)
    return HttpResponse(response)

def get_brands(request):
    url = "https://v1-sneakers.p.rapidapi.com/v1/sneakers"

    querystring = {"limit":"12","brand":request}

    headers = {
        "X-RapidAPI-Host": "v1-sneakers.p.rapidapi.com",
        "X-RapidAPI-Key": "a9c9774493mshf4df80a9e398926p1ffb86jsn33ae009aa91c"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)


def sneaker_brand(request,brand,page):
    url = "https://v1-sneakers.p.rapidapi.com/v1/sneakers"

    querystring = {"limit":"16","brand":brand,"page":page}

    headers = {
	"X-RapidAPI-Host": "v1-sneakers.p.rapidapi.com",
	"X-RapidAPI-Key": "a9c9774493mshf4df80a9e398926p1ffb86jsn33ae009aa91c"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(brand)
    # print(page)
    
    return HttpResponse(response)


@csrf_exempt
def add_user(request):
        if(request.method=='POST'):
            print('reached add user endpoint')
            d=json.loads(request.body)
            # print(d['name'])
            data=User(firstname=d['name'],lastname='sneak',email=d['mail'],password=d['password'])
            if(User.objects.filter(email=d['mail']).exists()):
                print('email taken')
                return JsonResponse({'message':'USER EXISTS'})
            else:
                data.save()
                print('added user')
                return JsonResponse({'message': 'ADDED USER'})

@csrf_exempt
def login(request):
    if(request.method=='POST'):
        d=json.loads(request.body)
        if(User.objects.filter(email=d['mail'],password=d['password']).exists()):
            item=User.objects.filter(email=d['mail'],password=d['password']).values()
            # data=serializers.serialize('json',item[0])
            print(item)
            return JsonResponse({'message':'LOGGED IN','data':item[0]})
            
        else:
            return JsonResponse({'message':'INCORRECT'})