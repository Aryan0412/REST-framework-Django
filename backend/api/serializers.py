from  rest_framework import serializers
from .models import Product
from .serializers import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            # 'get_discount',
            'my_discount'
        ]

    def get_my_discount(self, obj):
        return obj.get_discount()