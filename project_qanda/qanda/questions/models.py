from django.db import models

class Question(models.Model):
    """
    Question Model.
    """

    text = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text