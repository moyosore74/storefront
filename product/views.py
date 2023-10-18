from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework.decorators import api_view
import json

product_list = { 
}

@api_view(['GET'])
def get_product(request):
    return JsonResponse(product_list)

@api_view(['POST'])
def create_product(request):
    raw_body = request.body
    raw_data = json.loads(raw_body)
    id = len(product_list)+1
    product_list[id] = raw_data
    return JsonResponse(raw_data)

@api_view(['GET'])
def single_product(request, id):
    return JsonResponse(product_list[id])

@api_view(['PUT'])
def update_product(request, id):
    raw_body = request.body
    raw_data = json.loads(raw_body)
    product_list[id] = raw_data
    return JsonResponse(product_list[id])

@api_view(['DELETE'])
def delete_product(request, id):
    del product_list[id]
    return JsonResponse({})