from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Poll, Question, Option, Answer


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = [
            'id',
            'question',
            'text',
        ]

    def create(self, validated_data):
        question = validated_data.get('question')
        if question.type_answer == Question.TEXT:
            raise ValidationError(detail='Question Type "TEXT",  please without Options')
        return super().create(validated_data)


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            'id',
            'poll',
            'text',
            'type_answer',
            'options',
        ]


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class PollDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = [
            'id',
            'author',
            'title',
            'start_date',
            'end_date',
            'description',
            'questions',
        ]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'user',
            'question',
            'options',
            'text_answer',
        ]
