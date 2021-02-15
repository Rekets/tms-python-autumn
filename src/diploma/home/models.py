from django.contrib.auth.models import User
from django.db import models


class Home(models.Model):
    def home(request):
        pass


class Articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title} - {self.content[:50]}...'
