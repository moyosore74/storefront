from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework.decorators import api_view
import json

user_profile = { "name" : "John", 
      "age" : "27" ,
      "email" : "John21@gmaiil.com"
}

@api_view(['POST'])
def say_hello(request):
    return HttpResponse('Hello World')

@api_view(['PUT' , 'POST'])
def say_hi(request):
    return JsonResponse(user_profile)

@api_view(['POST'])
def payload(request):
    username = request.POST.get('Username')
    password = request.POST.get('Password')
    email = request.POST.get('Email')
    print(username)
    print(password)
    print(email)
    return JsonResponse({"name" : "Ade"})

@api_view(['POST'])
def handle_form_data(request):
    username = request.POST.get('Username')
    password = request.POST.get('Password')
    email = request.POST.get('Email')
    print(username)
    print(password)
    print(email)
    return JsonResponse({})

@api_view(['POST'])
def my_view(request):
    raw_body = request.body
    print(raw_body)
    raw_data = json.loads(raw_body)
    raw_data['name'] = 'Ade'
    return JsonResponse(raw_data)