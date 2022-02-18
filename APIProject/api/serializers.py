from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Article
from rest_framework.authtoken.models import Token


# create and update methods are already available in this
class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'description']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        # extra kwargs is used to pass extra context data to serializers
        extra_kwargs = {'password':{
            'write_only': True,
            'required': True
        }}

    # default create function just creates a new object to model
    # but in the case of user creation we want its create_user function to be called instead of create function
    # and also want to generate token for the new user
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
