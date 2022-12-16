from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"




class ChangePriceSerializers(serializers.Serializer):
    old_price = serializers.CharField(max_length = 25)
    new_price = serializers.CharField(max_length = 25)