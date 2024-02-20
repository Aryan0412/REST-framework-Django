import json
from django.shortcuts import render
from .models import Product
from django.forms.models import model_to_dict
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

from .serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    # print(request.data)
    if instance:
        # data = model_to_dict(model_data, fields = ['id', 'title', 'price', 'sale_price'])
        data = ProductSerializer(instance).data
       
    return Response(data)