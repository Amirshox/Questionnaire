from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserListSerializer, UserCreateUpdateSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer

    def get_serializer_class(self):
        if self.action in ('get', 'retrieve'):
            return UserListSerializer
        return super().get_serializer_class()
