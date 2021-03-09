from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, DetailView
import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
from home.models import Articles


def home(request):
    return render(request, "home.html", {"home": home})


def start_work(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=06a9524d385dce1ede0aa8da5fcb9d65'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'start.html', context)


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
