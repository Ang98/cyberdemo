""" Usuarios serializers"""
# Django
from django.contrib.auth import authenticate, password_validation
from django.core.validators import RegexValidator
from django.utils import timezone
from django.conf import settings

# Rest Framework
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from usuarios.models import Usuario

# Models
from api.models.Externo import Externo

# Utilities
import jwt
from datetime import timedelta


class UsuariorModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Usuario
        fields = (
            'id',
            'username',
            'is_externo',
            'is_administrador',
            'is_militante'
        )


class UsuarioSignupSerializer(serializers.Serializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Usuario.objects.all())])

    dni = serializers.CharField(
        validators=[UniqueValidator(queryset=Usuario.objects.all())])

    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=Usuario.objects.all())]
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = serializers.CharField(validators=[phone_regex])

    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):
        """Verify passwords match."""
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Contraseñas Diferentes.")
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        """Handle user and profile creation."""
        data.pop('password_confirmation')
        data['is_externo'] = True
        user = Usuario.objects.create_user(**data)
        Externo.objects.create(usuario=user)
        return user

    def gen_token(self, usuario):
        exp_date = timezone.now() + timedelta(days=3)
        pay_load = {
            'user': usuario.username,
            'exp': int(exp_date.timestamp()),
            'type': 'tipo'
        }
        token = jwt.encode(pay_load, settings.SECRET_KEY, algorithm='HS256')
        return token.decode()


class UsuarioLoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):

        usuario = authenticate(
            username=data['username'], password=data['password'])

        if not usuario:
            raise serializers.ValidationError('Ivalid redentials')

        self.context['user'] = usuario
        return data

    def create(self, data):

        token, created = Token.objects.get_or_create(user=self.context['user'])

        return self.context['user'], token.key
