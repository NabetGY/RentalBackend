from django.db.models import query
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken

from rooms.serializers import RoomSerializer, RoomListSerializer, UpdateRoomSerializer
from users.models import UserProfile
from rooms.models import Images


class RoomViewSet( ModelViewSet ):
    serializer_class = RoomSerializer
    queryset = RoomSerializer.Meta.model.objects.all()

    #permission_classes = ( IsAuthenticated,)

    def get_user( self, email ):
        user = UserProfile.objects.filter( email = email ).first()
        print( user )
        return user
    
    def save_images( self, room, images ):
        for image in images:
            Images.objects.create( room = room, image = image )
        return True

    def list( self, request ):
        email=request.GET.get('email')
        if(email==None):
            rooms = RoomListSerializer( self.get_queryset(), many = True )
            return Response( rooms.data, status = status.HTTP_200_OK )
        else:
            user = self.get_user(email)
            query = self.serializer_class.Meta.model.objects.filter(user=user)
            rooms = RoomListSerializer( query, many = True )
            return Response( rooms.data, status = status.HTTP_200_OK )


    def create( self, request ):
        # send information to serializer
        data = request.data.copy()
        data[ 'user' ] = self.get_user( data.get( 'user' ) ).pk
        serializer = self.serializer_class( data = data )
        if serializer.is_valid():
            room = serializer.save()
            return Response(
                { 'message': 'Producto creado correctamente!'},
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status = status.HTTP_400_BAD_REQUEST
        )

    def update( self, request, *args, **kwargs ):
        print('llegue')
        id = request.data.get('id')
        habitacion = self.get_queryset().filter(pk=id).first()
        if habitacion:
            # send information to serializer referencing the instance
            serializer = UpdateRoomSerializer(
                habitacion, data = request.data
            )
            if serializer.is_valid():
                serializer.save()
                return Response( serializer.data, status = status.HTTP_200_OK )
            return Response(
                serializer.errors, status = status.HTTP_400_BAD_REQUEST
            )
    def destroy(self, request, pk=None):
        try:        
            self.get_object().delete()
            return Response({'message':'Publicacion eliminada correctamente!'}, status=status.HTTP_200_OK)       
        except self.get_object().DoesNotExist:
            return Response({'message':'', 'error':'Publicacion no encontrada!'}, status=status.HTTP_400_BAD_REQUEST)
