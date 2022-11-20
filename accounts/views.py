from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.views import generic
from django.contrib.auth import login, authenticate

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import generics
from rest_framework.exceptions import Throttled

from .serializers import  ProfileSerializer , VerifyEmailSerializer , UserSerialization , ChangeMobileSerializer
from .models import Profile , VerifyEmail, VerifyMobile


# Create your views here.



class LoginView(APIView):
    queryset = User.objects.all()

    error_messages = {
        'invalid': "Invalid username or password",
        'disabled': "Sorry, this account is suspended",
    }

    def get(self, request):
        ser_data = LoginSerializer(data=request.POST)
        return Response(data=ser_data.data)

    def _error_response(self, message_key):
        data = {
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
        }

    def post(self, request):
        context ={
           'email' : str(request.POST.get('email')),
           'password' : str(request.POST.get('password'))
        }
        user = authenticate(context)
        if user is not None:
            if user.is_active:
                login(request, user)
        return Response(data = context)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



class ListUsersViews(APIView):

    def get(self , request):
        users = User.objects.all()
        ser_data = UserSerialization(instance = users , many = True)
        return Response(data = ser_data.data , status = status.HTTP_200_OK)


class Register(APIView):

    def post(self , request):
        ser_data = ProfileSerializer(instance = Profile , data = request.POST)

        if ser_data.is_valid(raise_exception = True):
            Profile.objects.create(
                first_name = ser_data.validated_data['first_name'],
                last_name = ser_data.validated_data['last_name'],
                mobile = ser_data.validated_data['mobile'],
            )

            return Response(data = ser_data.data , status = status.HTTP_201_CREATED)

        else:
           return Response(ser_data.errors , status = status.HTTP_404_NOT_FOUND)



def validate_data(data = Profile , new_mobile = None ):
      mobile = VerifyMobile.objects.filter(email = data.email , mobile = data.mobile).first()
      if mobile and not new_mobile:
          if mobile.is_expired():
              mobile.delete()
              mobile = VerifyMobile.objects.create(email = data.email , mobile = data.mobile)

          if mobile.verify:
              return Response({'was successfuly verified'})


          else:
              raise Throttled(detail =_('you can recieve request in 60 seconds'))




class ChangeMobile(APIView):

    permission_classes = [AllowAny ,]

    def post(self , request):
        ser_data = ChangeMobileSerializer(data = request.data)

        if ser_data.is_valid(raise_exception = True):
            profile = Profile.objects.filter(mobile = ser_data.validated_data['old_mobile']).first()

            if profile:
                mobile = validate_data(data = Profile , new_mobile = ser_data.validated_data['new_mobile'])
                profile.mobile = mobile.mobile

                profile.save()
















