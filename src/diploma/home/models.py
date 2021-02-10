from django.db import models


class Home(models.Model):
    def home(request):
        pass


class Articles(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.content}...'
