from django.db import models

class freeBoard_content(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class freeBoard_answer(models.Model):
    title = models.ForeignKey(freeBoard_content, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
