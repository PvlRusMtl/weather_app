import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
from django.http import HttpResponseRedirect



def index(request):
    appid = '731dedad41dea0f6b5713b05ac1c6a1d'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    form = CityForm(request.POST or None)
    if(request.method == 'POST'):        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    
    cities = City.objects.all()

    all_cities = []
    
    for city in cities:
        res = requests.get(url.format(city.name)).json()        
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res['weather'][0]['icon']
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)
