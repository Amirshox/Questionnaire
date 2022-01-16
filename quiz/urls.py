# Django
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

# Project
from .views import PollViewSet, QuestionViewSet, OptionViewSet, AnswerViewSet

router = DefaultRouter()

router.register('polls', PollViewSet, 'polls')
router.register('questions', QuestionViewSet, 'questions')
router.register('options', OptionViewSet, 'options')
router.register('answers', AnswerViewSet, 'answers')

urlpatterns = router.urls
