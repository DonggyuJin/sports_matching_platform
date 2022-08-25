from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=20, unique=True)
    phonenumber = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=200, blank=True)
    favorite = models.CharField(max_length=200, blank=True)
    introduction = models.TextField(max_length=2000, blank=True)
    auth = models.CharField(max_length=10, verbose_name="인증번호", null=True)
    score = models.IntegerField(default=0)
    tier = models.CharField(max_length=200, blank=True)