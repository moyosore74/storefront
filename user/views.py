from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework.decorators import api_view
import json

user_list = { 

}

@api_view(['GET'])
def get_user(request):
    return JsonResponse(user_list)

@api_view(['POST'])
def create_user(request):
    raw_body = request.body
    raw_data = json.loads(raw_body)
    id = len(user_list)+1
    user_list[id] = raw_data
    return JsonResponse(raw_data)

@api_view(['GET'])
def single_user(request, id):
    return JsonResponse(user_list[id])

@api_view(['PUT'])
def update_user(request, id):
    raw_body = request.body
    raw_data = json.loads(raw_body)
    user_list[id] = raw_data
    return JsonResponse(user_list[id])

@api_view(['DELETE'])
def delete_user(request, id):
    del user_list[id]
    return JsonResponse({})