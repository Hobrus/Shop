from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GoodsSerializer
from .models import Goods
from abc import ABC


# Create your views here.
class GoodsViewSet(viewsets.ModelViewSet):
    serializer_class = GoodsSerializer
    queryset = Goods.objects.all()