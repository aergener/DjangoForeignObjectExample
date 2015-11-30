from app import models as app_models
from rest_framework.serializers import ModelSerializer

class PriceSerializer(ModelSerializer):
    class Meta:
        model = app_models.Price
        fields = ('price',)

class StockSerializer(ModelSerializer):
    price = PriceSerializer(many=False)

    class Meta:
        model = app_models.Stock

    def create(self, validated_data):
        price_data = validated_data.pop('price')
        stock = app_models.Stock.objects.create(**validated_data)
        app_models.Price.objects.create(stock=stock, **price_data)
        return stock
