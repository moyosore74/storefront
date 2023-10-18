from django.urls import path 
from . import views


# URLConf
urlpatterns = [
    path('get_user', views.get_user),
    path('create_user', views.create_user),
    path('single_user/<int:id>', views.single_user),
    path('update_user/<int:id>', views.update_user),
    path('delete_user/<int:id>', views.delete_user)
]

