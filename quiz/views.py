from uuid import uuid1

from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from users.models import User
from .models import Poll, Question, Option, Answer
from .serializers import PollSerializer, QuestionSerializer, OptionSerializer, AnswerSerializer, PollDetailSerializer


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


class UserPollAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')

        queryset = Poll.objects.filter(questions__answers__user_id=user_id).distinct()

        serializer = PollSerializer(queryset, many=True)
        return Response(serializer.data)


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PollDetailSerializer
        return super().get_serializer_class()


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class AnswerViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        if not request.data.get('user'):
            username = str(uuid1())
            user = User.objects.create(username=username)
            request.data['user'] = user.id
        return super().create(request, *args, **kwargs)
