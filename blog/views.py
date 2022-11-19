from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework import status


from .serializers import  BlogSerializers
from .models import Blog
# Create your views here.

class ListViewsBlogs(APIView):

    def get(self , request):
        blogs  = Blog.objects.all()
        ser_data = BlogSerializers(instance = blogs , many=True)
        return Response(data = ser_data.data)


class CreateViewBlog(APIView):

    def post(self , request):
        users_id = User.objects.values_list('id' , flat = True)
        ser_data = BlogSerializers(instance = Blog , data = request.POST)
        if ser_data.is_valid():

            Blog.objects.bulk_create(
                Blog(
                    user_id = uid,
                    title = ser_data.validated_data['title'],
                    text = ser_data.validated_data['text'],
                )
                for uid in users_id)


            return Response(data = ser_data.data)


        return Response(ser_data.errors)



class UpdateViewBlog(APIView):

    def put(self , request , blog_id):
        users_ids = User.objects.values_list('id' , flat = True)
        blog = Blog.objects.get(pk = blog_id )
        ser_data = BlogSerializers(instance = blog , data = request.POST)

        if ser_data.is_valid():
            ser_data.save()

            return Response(data = ser_data.data)

        return Response(ser_data.errors)
