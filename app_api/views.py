from django.shortcuts import render
from django.http import JsonResponse

from .models import Info

# Create your views here.
def home(request, *args, **kwargs) -> JsonResponse:
    info_object = Info.objects.all()
    
    inform = [
        {
            "name":info.name,
            "age":info.age,
            "is_created":info.date_created,
            "is_updated":info.date_updated
        }
        for info in info_object
    ] 
    
#     data =[
#         {
#         "name":"Mariam",
#         "age":18,
#         "sch":"Futminna"
#     }
#    ]
    return JsonResponse(data=inform, safe=False)