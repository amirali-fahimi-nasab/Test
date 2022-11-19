from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Blog , Comment



class BlogSerializers(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = "__all__"
        extra_kwargs = {'title':{'required':True}}





class CommentSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = Comment
        fields = "__all__"

