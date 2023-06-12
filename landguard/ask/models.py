from django.db import models
#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 my open ai key
# Create your models here.

class Question (models.Model):
    # question_id = models.Index
    user_question = models.TextField()

    def __str__(self):
        return self.id


