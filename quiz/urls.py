# Django
from rest_framework.routers import DefaultRouter

# Project
from .views import PollViewSet, QuestionViewSet, OptionViewSet, AnswerViewSet

router = DefaultRouter()

router.register('polls', PollViewSet, 'polls')
router.register('questions', QuestionViewSet, 'questions')
router.register('options', OptionViewSet, 'options')
router.register('answers', AnswerViewSet, 'answers')

urlpatterns = router.urls
