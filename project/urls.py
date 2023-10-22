from django.urls import path 
from . import views


# URLConf
urlpatterns = [
    path('get_project', views.get_project),
    path('create_project', views.create_project)
]

