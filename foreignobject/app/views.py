from app import models as app_models
from app import serializers as app_serializers
from rest_framework import generics

class StockListView(generics.ListCreateAPIView):
    serializer_class = app_serializers.StockSerializer
    queryset = app_models.Stock.objects.all()
