from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.views import generic
from django.contrib.auth import login, authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import generics
from rest_framework.exceptions import Throttled
from rest_framework.viewsets import ViewSet
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import generics

from .serializers import ProfileSerializer, VerifyEmailSerializer, UserRegistrationSerializers, ChangeMobileSerializer, \
    ChangPasswordSerializer, LoginSerializer, ChangeUsernameSerializer
from .models import Profile, VerifyEmail, VerifyMobile, ChangePassword


# Create your views here.





def validate_data(data=Profile, new_mobile=None):
    mobile = VerifyMobile.objects.filter(email=data.email, mobile=data.mobile).first()
    if mobile and not new_mobile:
        if mobile.is_expired():
            mobile.delete()
            mobile = VerifyMobile.objects.create(email=data.email, mobile=data.mobile)

        if mobile.verify:
            return Response({'was successfuly verified'})


        else:
            raise Throttled(detail=_('you can recieve request in 60 seconds'))


class ChangeMobile(APIView):

    def post(self, request):
        ser_data = ChangeMobileSerializer(instance=Profile, data=request.data)
        if ser_data.is_valid(raise_exception=True):
            mobile = Profile.objects.get(mobile=ser_data.validated_data['old_mobile'])

            if mobile:
                new_mobile = ser_data.validated_data['new_mobile']
                mobile.mobile = new_mobile

                return Response({'status': 'Your mobile was changed'})

        return Response(ser_data.errors, status=404)


@api_view(['GET', ])
def list_users(request):
   users = User.objects.all()
   ser_data = UserSerialization(instance = users , many=True)
   return Response(data = ser_data.data)

class RegisterUser(APIView):

    def post(self, request):
        ser_data = UserRegistrationSerializers(data=request.data)

        if ser_data.is_valid(raise_exception=True):
            User.objects.create_user(
                first_name = ser_data.validated_data['first_name'],
                last_name = ser_data.validated_data['last_name'],
                email = ser_data.validated_data['email'],
                phone_number = ser_data.validated_data['phone_number'],
                address = ser_data.validated_data['address'],
                national_id = ser_data.validated_data['national_id'],
            )

            return Response(data=ser_data.data, status=201)

        return Response(ser_data.errors, status=404)


class CreateSuperUser(APIView):
    def post(self , request):
        ser_data = UserRegistrationSerializers(data = request.data)
        if ser_data.is_valid():
            User.objects.create_superuser(username = ser_data.validated_data['username'],
                                          email = ser_data.validated_data['email'],
                                          password = ser_data.validated_data['password']
                                          )

            return Response(data = ser_data.data , status = 201)

        return Response(ser_data.errors , status=401)


class ChangePasswordView(APIView):

    def put(self , request , user_id):
        user = User.objects.get(id = user_id)
        ser_data = UserSerialization(instance = user , data = request.data)

        if ser_data.is_valid():
            user.set_password(ser_data.validated_data['password'])
            user.save()
            return Response({'status':'your password was changed'} , status = 200)

        else:
            return Response(ser_data.errors , status=404)




class Logout(APIView):

    def get_object(self):
        obj = self.request.user
        return obj


    def put(self , request):
        self.obj = self.get_object()
        self.obj.is_active = False
        self.obj.save()
        return Response({'massage':'you logged out'})



class ChangeUsername(APIView):

    def put(self , request , pk):
        user = User.objects.get(id = pk)
        ser_data = ChangeUsernameSerializer(instance = user , data = request.data)
        if ser_data.is_valid():
            if ser_data.validated_data['old_username'] :
                user.username = ser_data.validated_data['new_username']
                user.save()
                return Response({'status':'your username was changed'} , status=200)


        return Response(ser_data.errors , status=404)




class DeleteUser(APIView):

    def delete(self , request , pk):
        user = User.objects.get(id = pk)
        user.delete()
        return Response('Your user was deleted')



