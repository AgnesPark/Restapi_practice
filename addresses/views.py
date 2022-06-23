from ast import Add
from typing_extensions import dataclass_transform
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Addresses
from .serializers import AddressSerializer
from rest_framework.parsers import JSONParser


@csrf_exempt
def addresses_list(request):
    if request.method == 'GET':
        query_set = Addresses.objects.all()
        serializer = AddressSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def address(request, pk):

    data = Addresses.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = AddressSerializer(data)
        return JsonResponse(serializer.data, safe=False)

#    elif request.method == 'POST':
#        data = JSONParser().parse(request)

#        serializer = AddressSerializer(data=data)
#        if serializer.is_valid():
##            serializer.save()
 #           return JsonResponse(serializer.data, status=201)
 #       return JsonResponse(serializer.errors, status=400)

 #   elif request.method == 'DELETE':
