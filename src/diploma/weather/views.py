import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
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
            'city': 'Minsk',
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        print(city_weather)
        print('***************')
        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/weather.html', context)
