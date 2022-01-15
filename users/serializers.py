from rest_framework import serializers

from .models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'rating',
        ]


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'is_superuser',
            'is_staff',
            'date_joined',
            'last_login',
            'groups',
            'user_permissions'
        ]
