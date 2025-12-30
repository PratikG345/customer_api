from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Customer,Order
from .serializer import CustSerializer,OrderWriteSerializer,OrderReadSerializer
# Create your views here.

@api_view(['GET'])
def get_customer(req):
    cust = Customer.objects.all()
    ser = CustSerializer(cust,many=True)
    return Response(ser.data)

@api_view(['POST'])
def add_customer(req):
    ser = CustSerializer(data=req.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data,status=status.HTTP_201_CREATED)
    return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_order(req):
    order = Order.objects.all()
    ser = OrderReadSerializer(order,many=True)
    return Response(ser.data)

@api_view(['POST'])
def add_order(req):
    ser = OrderWriteSerializer(data=req.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data,status=status.HTTP_201_CREATED)
    return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def order_detail(req,pk):
    order = get_object_or_404(Order,pk=pk)
    if req.method == 'GET':
        ser= OrderWriteSerializer(order)
        return Response(ser.data)
    
    if req.method == 'PUT':
        ser=OrderWriteSerializer(order,data=req.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_200_OK)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if req.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
