from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework import status
from rest_framework.permissions import AllowAny


from .serializers import  BlogSerializers
from .models import Blog
# Create your views here.

@api_view(['GET',])
@permission_classes((AllowAny , ))
def list_views_blogs(request):
    blogs = Blog.objects.all()
    ser_data = BlogSerializers(instance = blogs , many=True)
    return Response(data = ser_data.data)


