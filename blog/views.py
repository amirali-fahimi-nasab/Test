from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import views , viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated , AllowAny

from .models import Blog
from .serializers import BlogSerializers
# Create your views here.

class BlogViews(viewsets.ViewSet):

    @permission_classes([AllowAny , ])
    def list(self , request):
        blogs = Blog.objects.all()
        ser_data = BlogSerializers(instance=blogs , many=True)
        return Response(data = ser_data.data)

    @permission_classes([IsAuthenticated])
    def create(self , request):
        ser_data = BlogSerializers(data = request.data)
        if ser_data.is_valid():
            ser_data.validated_data['writer'] = request.user
            ser_data.save()
            return Response({"massage":"Your blog was created"} , status=201)

        else:
            return Response(ser_data.errors , status=404)




    @permission_classes([IsAuthenticated ,])
    def update(self , request , blog_id):
        blog  = Blog.objects.get(id = blog_id)
        ser_data = BlogSerializers(instance = blog , data = request.data , partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data , status = 200)

        return Response(ser_data.errors  ,status = 404)


    @permission_classes([IsAuthenticated ,])
    def destroy(self , request , blog_id):
        blog = Blog.objects.get(id = blog_id)
        blog.delete()
        return Response({'massage':'Your blog was deleted'})
