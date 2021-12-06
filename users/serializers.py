from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from users.models import UserProfile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainSerializer( TokenObtainPairSerializer ):

    class Meta:
        model = UserProfile
        fields = ( 'email', 'username' )


class CustomUserSerializer( serializers.ModelSerializer ):

    class Meta:
        model = UserProfile
        fields = ( 'username', 'email', 'image_perfil', 'number_phone' )


class UserSerializer( serializers.ModelSerializer ):

    class Meta:
        model = UserProfile
        fields = '__all__'

    def create( self, validated_data ):
        instance = UserProfile( **validated_data )
        instance.set_password( validated_data.get( 'password' ) )
        instance.save()
        return instance

    ''' def validate_email(self, data):
        print(data)
        users = UserProfile.objects.filter(email = data)
        if len(users) != 0:
            raise serializers.ValidationError("Este email de usuario ya existe, ingrese uno nuevo...")
        else:
            return data '''


class UpdateUserSerializer( serializers.ModelSerializer ):

    class Meta:
        model = UserProfile
        fields = ( 'username', 'image_perfil', 'number_phone' )
        lookup_field = "email"


class CardUserSerializer( serializers.ModelSerializer ):
    
    class Meta:
        model = UserProfile
        fields = ( 'username', 'image_perfil', 'number_phone', 'is_subscribed' )
