from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.

class UserProfileManager(BaseUserManager):
    """ Manager para perfiles de usuario """

    def create_user(self, email, username, password=None):
        """ Crer un nuevo User Profile """
        if not email:
            raise ValueError('Usuario debe tener un Email')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    ''' modelo base de datos para usuarios en el sistema '''
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_subscribed = models.BooleanField(default=False)
    image_perfil = models.URLField()
    number_phone = models.CharField(max_length=10)
    positive_points = models.IntegerField(default=0)
    negative_points = models.IntegerField(default=0)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email'] 

    def get_full_name(self):
        """ obtener nombre de usuario completo """
        return self.username

    def get_short_username(self):
        """ obtener nombre corto del usuario """
        return self.username
    
    def __str__(self):
        """ Retorna Cadena representando nuestro usuario """
        return self.email