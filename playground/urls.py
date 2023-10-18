from django.urls import path 
from . import views


# URLConf
urlpatterns = [
    path('hello', views.say_hello),
    path('hi' , views.say_hi),
    path('payload', views.payload),
    path('data', views.handle_form_data),
    path('rawr', views.my_view)
]

