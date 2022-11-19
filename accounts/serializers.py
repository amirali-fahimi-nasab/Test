from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Profile , VerifyEmail


class UserSerialization(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username' , 'email' ,'password']



class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['first_name' , 'last_name' , 'mobile']



class ChangeMobileSerializer(serializers.Serializer):
    old_mobile = serializers.CharField(max_length = 17)
    new_mobile = serializers.CharField(max_length = 17)




class VerifyEmailSerializer(serializers.Serializer):
    old_email = serializers.CharField(max_length = 50 , required = True)
    new_email = serializers.CharField(max_length = 50 , required = True)



