from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from rooms.models import Room, Images
from users.serializers import CardUserSerializer


class ImagesSerializer( ModelSerializer ):
    
    class Meta:
        model = Images
        fields = ['image']


class RoomSerializer( ModelSerializer ):

    images = ImagesSerializer(many=True )

    class Meta:
        model = Room
        fields = [
            'titulo', 'area', 'banio', 'ciudad', 'ubicacion', 
            'descripcion', 'estrato', 'precio', 'estacionamiento', 'user',
            'created_data', 'modified_data', 'deleted_data', 'images', 'id'
        ]

    def create(self, validated_data):
        print(validated_data)
        images_data = validated_data.pop('images')
        room = Room.objects.create(**validated_data)
        for image_data in images_data:
            Images.objects.create(room=room, **image_data)
        return room

class RoomListSerializer( ModelSerializer ):
    
    images = ImagesSerializer(many=True )
    user = CardUserSerializer()

    class Meta:
        model = Room
        fields = [
            'titulo', 'area', 'banio', 'ciudad', 'ubicacion', 
            'descripcion', 'estrato', 'precio', 'estacionamiento', 'user',
            'created_data', 'modified_data', 'deleted_data', 'images', 'id'
        ]



class UpdateRoomSerializer( ModelSerializer ):
    
    images = ImagesSerializer(many=True )

    class Meta:
        model = Room
        fields = [
            'titulo', 'area', 'banio', 'ciudad', 'ubicacion', 
            'descripcion', 'estrato', 'precio', 'estacionamiento',
            'images',
        ]
        
    def update(self, instance, validated_data):
        images_data = validated_data.pop('images')
        instance = super().update(instance, validated_data)
        Images.objects.filter(room=instance.id).delete()
        for image_data in images_data:
            Images.objects.create(room=instance, **image_data)
        return instance
    
    
    ''' def create(self, validated_data):
        print(validated_data)
        images_data = validated_data.pop('images')
        room = Room.objects.create(**validated_data)
        images_data = validated_data.pop('images')
            Images.objects.create(room=room, **image_data)
        return room '''