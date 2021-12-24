from django.contrib import admin
from django.urls import path
from .views import get_personas, insert_persona, update_persona, delete_persona

urlpatterns = [
    path('get-personas', get_personas ),
    path('insert-persona', insert_persona),
    path('update-persona', update_persona),
    path('delete-persona', delete_persona),
]
