from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from home.models import Articles


def home(request):
    return render(request, "home.html", {"home": home})


def start_work(request):
    return render(request, "start.html", {"start": start_work})


class ArticleListView(ListView):
    model = Articles
    template_name = "articles.html"
    ordering = "title"
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    model = Articles
    template_name = "article.html"
    slug_field = "pk"
    context_object_name = "obj"
