from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework.decorators import api_view
import json

project_list = { 
}

@api_view(['GET'])
def get_project(request):
    return JsonResponse(project_list)

@api_view(['POST'])
def create_project(request):
    return JsonResponse(project_list)