from rest_framework.viewsets import ModelViewSet

from questions.models import Question, Response
from questions.serializers import QuestionSerializer, ResponseSerializer

class QuestionViewSet(ModelViewSet):
    """
    Question Modelviewset
    """

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class Response(models.Model):
    body = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    created = models.ForeignKey(Question, on_delete=models.CASCADE)

    created = models.ForeignKey(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class ResponseViewSet(ModelViewSet):
    """" Aquí mismo. Los atributos se pasan por la clase meta. Es exactamente lo mismo """

"""
api/casas/ LIST GET
api/casas/ CREATE POST

api/casas/1/ GET
api/casas/1/ DELETE
api/casas/1/ EDIT PUT
api/casas/1/ EDIT Parcial PATCH
"""
