from django.db import models


# Create your models here.
class EdgarModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)


class FeedbackModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    rating = models.IntegerField()
    feedback_text = models.TextField()
