# Django
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Project
from .views import PollViewSet, QuestionViewSet, OptionViewSet, AnswerViewSet, UserAnswerAPIView, UserPollAPIView

router = DefaultRouter()

router.register('polls', PollViewSet, 'polls')
router.register('questions', QuestionViewSet, 'questions')
router.register('options', OptionViewSet, 'options')
router.register('answers', AnswerViewSet, 'answers')

urlpatterns = [
    path('user/<int:user_id>/polls/', UserPollAPIView.as_view()),
    path('user/<int:user_id>/polls/<int:poll_id>/answers/', UserAnswerAPIView.as_view()),
    path('', include(router.urls)),
]
