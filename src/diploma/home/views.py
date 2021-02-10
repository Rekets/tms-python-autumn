from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from home.models import Articles


def home(request):
    return render(request, "home.html", {"home": home})


def all_articles(request):
    articles = Articles.objects.all()
    return render(request, "articles.html", {"articles": articles})


def get_article(request, pk: int):
    article = get_object_or_404(Articles, pk=pk)
    return render(
        request, "article.html", {"article": article}
    )
