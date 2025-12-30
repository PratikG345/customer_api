from rest_framework import serializers
from .models import Customer,Order

class CustSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
class OrderWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'    
       
       
class OrderReadSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    class Meta:
        model = Order
        fields = '__all__'    