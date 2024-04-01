from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import GoodsSerializer
from .models import Goods
from abc import ABC


# Create your views here.
class GoodsViewSet(viewsets.ModelViewSet):
    serializer_class = GoodsSerializer
    queryset = Goods.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
