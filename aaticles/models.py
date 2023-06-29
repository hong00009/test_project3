from django.db import models

# Create your models here.

class AAticle(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()

    # ☆저번과 달라진곳, 현재 시간을 자동으로 입력하는 기능 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)