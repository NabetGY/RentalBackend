from django.db import models
from cloudinary.models import CloudinaryField

from core import settings

# Create your models here.


class Room( models.Model ):
    TIPOS_BANIO = (
        ( 'P', 'Privado' ),
        ( 'C', 'Compartido' ),
    )

    titulo = models.CharField( 'Titulo', max_length = 50 )
    area = models.IntegerField( "Area en mts" )
    banio = models.CharField( "Baño ", max_length = 1, choices = TIPOS_BANIO )
    ciudad = models.CharField( "Ciudad", max_length = 50 )
    ubicacion = models.CharField( "Ubicacion aproximada", max_length = 50 )
    descripcion = models.TextField( "Breve Descripcion",)
    estrato = models.IntegerField( "Estrato socioeconomico" )
    precio = models.IntegerField( "Precio" )
    estacionamiento = models.BooleanField( "Estacionamiento" )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete = models.CASCADE
    )
    created_data = models.DateField(
        "Fecha de Creacion", auto_now = False, auto_now_add = True
    )

    modified_data = models.DateField(
        "Fecha de Modificacion", auto_now = False, auto_now_add = True
    )

    deleted_data = models.DateField(
        "Fecha de Eliminacion", auto_now = False, auto_now_add = True
    )

    def __str__( self ):
        return self.titulo

    class Meta:
        verbose_name = 'Modelo Room'
        verbose_name_plural = 'Modelos Room'


class Images( models.Model ):
    room = models.ForeignKey( Room, related_name='images', on_delete = models.CASCADE )
    image = models.URLField( 'imagen' )
