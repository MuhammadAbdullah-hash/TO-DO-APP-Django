from django.urls import path , include
from . import views


urlpatterns = [
    path('' , views.main_app , name = 'home-app'),
	path('delete_item/' , views.delete_item , name = 'delete_item'),    
	path('edit_item/' , views.edit_item , name = 'edit_item'),
]


