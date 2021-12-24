from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from rest_framework import status
from .models import Persona
import json

# Create your views here.

def get_personas(request):
    """Retorna todos los datos del modelo persona"""
    if request.method == 'GET':
        try:
            data = json.loads(serializers.serialize('json',Persona.objects.all().order_by('id')))
            print(data)
            response = {
                    'data': data ,
                    'error': False,
                    'message': 'Se retornan registros de modelo persona' if data else 'No se encontraron registros'
                }
            return JsonResponse(response, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            response = {
                'error': True,
                'message': f'Error al modificar los datos: {str(e)}'
            }
            return JsonResponse(response, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt 
def insert_persona(request):
    """Inserta un nuevo registro en el modelo persona"""
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            new_entry = Persona(tipo_documento = body["data"]["tipo_documento"],
                                documento      = body["data"]["documento"],
                                nombres        = body["data"]["nombres"],
                                apellidos      = body["data"]["apellidos"],
                                hobbie         = body["data"]["hobbie"]
                                )
            new_entry.save()
            response = {
                    'error': False,
                    'message': 'Se realiza registro exitosamente'
                }
            return JsonResponse(response, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            response = {
                'error': True,
                'message': f'Error al insertar persona: {str(e)}'
            }
            return JsonResponse(response, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@csrf_exempt 
def update_persona(request):
    """Actualiza multiples registros en el modelo personas filtrando por el id de cada fila"""
    if request.method == 'PUT':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            id = body["id"]
            Persona.objects.filter(id=id).update(
                                tipo_documento = body["data"]["tipo_documento"],
                                documento      = body["data"]["documento"],
                                nombres        = body["data"]["nombres"],
                                apellidos      = body["data"]["apellidos"],
                                hobbie         = body["data"]["hobbie"]
                                )                
            response = {
                    'error': False,
                    'message': 'Se realiza actualizacion exitosamente'
                }
            return JsonResponse(response, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            response = {
                'error': True,
                'message': f'Error al editar persona: {str(e)}'
            }
            return JsonResponse(response, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@csrf_exempt 
def delete_persona(request):
    """Elimina multiples registros en el modelo personas filtrando por el id de cada fila"""
    if request.method == 'DELETE':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            id = body['id']
            Persona.objects.filter(id=id).delete()
            response = {
                    'error': False,
                    'message': 'Se elimina persona exitosamente'
                }
            return JsonResponse(response, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            response = {
                'error': True,
                'message': f'Error al eliminar persona: {str(e)}'
            }
            return JsonResponse(response, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

