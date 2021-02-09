from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from home.models import Article


def home(request):
    return render(request, "home.html", {"home": home})


def all_articles(request):
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles": articles})


def get_articles(request, pk):
    article = get_object_or_404(pk=pk)
    return HttpResponse(article)
