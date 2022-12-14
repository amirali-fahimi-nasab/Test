from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action , api_view
from rest_framework import renderers

from .models import Blog
from .serializers import BlogSerializer
# Create your views here.


class BlogView(viewsets.ViewSet):


    @api_view(['GET',])
    def list_views_blogs(self , request):
        blogs = Blog.objects.all()
        ser_data = BlogSerializer(instance = blogs , many=True)
        return Response(data = ser_data.data)