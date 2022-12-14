from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny  ,IsAdminUser
from rest_framework.serializers import ValidationError

from .models import Product
from .serializers import ProductSerializer  ,ChangePriceSerializers
# Create your views here.


@api_view(['GET',])
@permission_classes((AllowAny,))
def list_views_product(request):
    products = Product.objects.all()
    ser_data = ProductSerializer(instance = products , many=True)
    return Response(data = ser_data.data)



@api_view(['GET',])
@permission_classes((AllowAny ,))
def show_object(request , product_id):
    try :
        product = Product.objects.get(id = product_id )                      #show specific object
        ser_data = ProductSerializer(instance = product )
        return Response(data = ser_data.data , status = 200)

    except Product.DoesNotExist:
        raise ValidationError('Your product does not exist')



@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def create_view_product(request):
    ser_data = ProductSerializer(data = request.data  )
    if ser_data.is_valid():
        ser_data.validated_data['user'] = request.user
        ser_data.save()
        return Response(ser_data.data , status=200)

    else:
        return Response(ser_data.errors , status=404)


@api_view(['Delete',])
@permission_classes((IsAdminUser,))
def delete_view_product(request , product_id):
    product = Product.objects.get(id = product_id)
    product.delete()
    ser_data.save()
    return Response({'massage':'your product was deleted'} , status = 200)



@api_view(['PUT',])
@permission_classes((IsAdminUser ,))
def update_view_product(request , product_id):
    product = Product.objects.get(id = product_id)
    ser_data = ProductSerializer(instance = product , data = request.data , partial = True)
    if ser_data.is_valid():
        ser_data.save()
        return Response({'massage':'Your product was updated'} , status = 200)

    return Response(ser_data.errors , status = 404)


class ChangePriceProduct(APIView):
    permission_classes = [IsAuthenticated ,]
    def put(self , request  ,product_id):
        product = Product.objects.get(id = product_id)
        ser_data = ChangePriceSerializers(instance = Product ,data = request.data )
        if ser_data.is_valid():
            if ser_data.validated_data['old_price']:
               product.price = ser_data.validated_data['new_price']
               product.save()

            return Response({'status':'Your price was changed'} , status=200)


        else:
            return Response(ser_data.errors , status =404)




