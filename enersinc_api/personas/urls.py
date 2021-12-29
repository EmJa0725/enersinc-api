from django.contrib import admin
from django.urls import path
from .views import get_persons, get_single_person, add_person, update_person, delete_person

urlpatterns = [
    path('get-persons', get_persons ),
    path('get-single-person/<int:id>', get_single_person),
    path('add-person', add_person),
    path('update-person/<int:id>', update_person),
    path('delete-person/<int:id>', delete_person),
]
