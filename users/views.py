from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from quiz.serializers import PollSerializer
from .models import User
from .serializers import UserListSerializer, UserCreateUpdateSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer

    def get_serializer_class(self):
        if self.action in ('get', 'retrieve'):
            return UserListSerializer
        return super().get_serializer_class()

    @action(methods=['get'], detail=True)
    def polls_author(self, request, pk=None):
        user = self.get_object()
        polls = user.polls.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)
