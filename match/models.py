from django.db import models
from common.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator

class MatchSports(models.Model):
    author = models.ForeignKey(CustomUser, related_name='author_match', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    sports_name = models.CharField(max_length=50)
    sports_date = models.DateField()
    address = models.CharField(max_length=200)
    max_apply = models.PositiveIntegerField(default=1, verbose_name='max_apply')
    apply_count = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(30),
            MinValueValidator(1)
        ]
     )
    apply_state = models.ManyToManyField(CustomUser, related_name='apply_count')
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    hits = models.PositiveIntegerField(default=1, verbose_name='hits')
    
    def __str__(self):
        return self.title

class UserApply(models.Model):
    user_check = models.CharField(max_length=20)
    match_check = models.IntegerField(default=0)