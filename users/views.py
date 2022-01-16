from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from quiz.models import Answer
from quiz.serializers import PollSerializer, AnswerSerializer
from .models import User
from .serializers import UserListSerializer, UserCreateUpdateSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer

    def get_serializer_class(self):
        if self.action in ('get', 'retrieve'):
            return UserListSerializer
        return super().get_serializer_class()

    @action(methods=['get'], detail=True)
    def polls(self, request, pk=None):
        user = self.get_object()
        polls = user.polls.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)


class UserAnswerAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        poll_id = kwargs.get('poll_id')

        queryset = Answer.objects.filter(user_id=user_id, question__poll_id=poll_id)

        serializer = AnswerSerializer(queryset, many=True)
        return Response(serializer.data)
