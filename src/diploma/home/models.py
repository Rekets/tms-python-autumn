from django.contrib.auth.models import User
from django.db import models


class Home(models.Model):
    def home(request):
        pass


class Articles(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to="images", null=True)

    def __repr__(self):
        return f"{self.title} - {self.content[:50]}"

    def __str__(self):
        return f"{self.title} - {self.content[:50]}"


class Image(models.Model):
    image = models.ImageField(upload_to="images", null=True)
    article = models.ForeignKey("Articles", on_delete=models.CASCADE)
