from django.urls import path, include
from rest_framework.routers import DefaultRouter

from questions.views import QuestionViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)

urlpatterns = router.urls