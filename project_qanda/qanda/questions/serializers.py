from rest_framework.serializers import ModelSerializer
from questions.models import Question


class QuestionSerializer(ModelSerializer):
    """
    Question serializer.
    """
    responses = ResponseSerializer(many=True, read_only=True)

    class Meta:
        model = Response
        fields = ['id', 'body', 'question']


class QuestionSerializer(ModelSerializer):
    """
    Question serializer.
    """
    responses = ResponseSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'responses']

        def create(self)
