from tkinter import CASCADE
from django.db import models
from common.models import CustomUser

class FreeContent(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author_content')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    recommend = models.ManyToManyField(CustomUser, related_name='recommend_content')

    def __str__(self):
        return self.subject

class FreeAnswer(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author_answer')
    title = models.ForeignKey(FreeContent, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    recommend = models.ManyToManyField(CustomUser, related_name='recommend_answer')

