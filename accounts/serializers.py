from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Profile , VerifyEmail , ChangePassword


class UserSerializer(serializers.Serializer):
    model  = User
    username = serializers.CharField(max_length = 60 , required = True)
    password = serializers.CharField(max_length = 24 , required = True)

class UserRegistrationSerializers(serializers.Serializer):
    first_name = serializers.CharField(max_length=200, required=True)
    last_name = serializers.CharField(max_length=200, required=True)
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(max_length=20 , required=True)
    address = serializers.CharField(max_length=400, required=True)
    national_id = serializers.IntegerField(required=True)

    date_created = serializers.DateTimeField()


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['first_name' , 'last_name' , 'mobile']



class ChangeMobileSerializer(serializers.Serializer):
    model = Profile
    old_mobile = serializers.CharField(max_length = 17)
    new_mobile = serializers.CharField(max_length = 17)





class VerifyEmailSerializer(serializers.Serializer):
    old_email = serializers.CharField(max_length = 50 , required = True)
    new_email = serializers.CharField(max_length = 50 , required = True)




class ChangPasswordSerializer(serializers.Serializer):

    model = User

    old_password = serializers.CharField( max_length=26 , required = True)
    new_password = serializers.CharField( max_length=26 , required = True)



class ChangeUsernameSerializer(serializers.Serializer):
    model = User

    old_username = serializers.CharField(max_length = 100 , required = True)
    new_username = serializers.CharField(max_length = 100 , required = True)

    def validate(self, attrs):
        if attrs['old_username'] == attrs['new_username']:
            raise serializers.ValidationError('is not same')

    def validated_new_username(self , obj):
        if obj == 'admin':
            raise serializers.ValidationError('Your username must not be admin')

        return obj

class LoginSerializer(serializers.Serializer):

    model = User
    username = serializers.CharField(max_length=26 , required=True)
    password = serializers.CharField(max_length=26 , required=True)



