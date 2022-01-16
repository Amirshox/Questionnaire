from uuid import uuid1

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from users.models import User
from .models import Poll, Question, Option, Answer
from .serializers import PollSerializer, QuestionSerializer, OptionSerializer, AnswerSerializer, PollDetailSerializer


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


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        if not request.data.get('user'):
            username = str(uuid1())
            user = User.objects.create(username=username)
            request.data['user'] = user.id
        return super().create(request, *args, **kwargs)
