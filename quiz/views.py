from rest_framework import viewsets

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
