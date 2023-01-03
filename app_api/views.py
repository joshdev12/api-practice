from django.shortcuts import render
from django.http import JsonResponse

from .models import Info

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializer import InfoSerializers


@api_view(['GET'])
def index(request, *args, **kwargs):
    infom = Info.objects.all()
    serialisers = InfoSerializers(infom, many=True)
    
    return Response(serialisers.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def index_details(request, pk, *args, **kwargs):
    infom_details = Info.objects.get(id=pk)
    serialiser = InfoSerializers(infom_details)
    
    return Response(serialiser.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def upload(request, *args, **kwargs):
    serialiser = InfoSerializers(data=request.data)
    
    if serialiser.is_valid():
        serialiser.save()
        return Response(serialiser.data, status=status.HTTP_201_CREATED)
    
    return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update(request, pk, *args, **kwargs,):
    infom_update = Info.objects.get(pk=pk)
    serializer =InfoSerializers(infom_update, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# Create your views here.

# def index(request, *args, **kwargs) -> JsonResponse:
#     info_object = Info.objects.all()
    
#     inform = [
#         {
#             "name":info.name,
#             "age":info.age,
#             "is_created":info.date_created,
#             "is_updated":info.date_updated
#         }
#         for info in info_object
#     ] 
    
# #     data =[
# #         {
# #         "name":"Mariam",
# #         "age":18,
# #         "sch":"Futminna"
# #     }
# #    ]
#     return JsonResponse(data=inform, safe=False)