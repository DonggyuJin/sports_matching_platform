from django.db import models

class FreeContent(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class FreeAnswer(models.Model):
    title = models.ForeignKey(FreeContent, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
