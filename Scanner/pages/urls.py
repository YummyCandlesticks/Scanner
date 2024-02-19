from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.index, name="index") 
]

# the "" will redirect you to this page, and then the specific URLs here will redirect you to other views/templates