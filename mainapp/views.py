from .models import Project, Dish, Sale, Cart, CartItem, SaleItem
from django.shortcuts import render
from datetime import datetime
import requests


def home_plus(request):
    return render(request, 'main/home_plus.html')

def news(request):
    api_key = '6e02347b36af4b8b9cfee8600ae04704'
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'  # URL de la API externa
    
    api_key_weather = '0e70d6549b8ca40bd844ef432cdebe38'
    url_weather = f'https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&appid={api_key_weather}'
    response = requests.get(url)
    response_weather = requests.get(url_weather)

    if response.status_code == 200 and response_weather.status_code == 200:
        datos = response.json()
        articles = datos.get('articles', [])
        
        datos_weather = response_weather.json()
        current_weather = datos_weather.get('current', {})
        print(current_weather)
        timezone = datos_weather.get('timezone', 'No data')

        # Convert timestamp to human-readable time
        sunrise = datetime.fromtimestamp(current_weather.get('sunrise')).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(current_weather.get('sunset')).strftime('%H:%M:%S')
        
        current_weather['sunrise'] = sunrise
        current_weather['sunset'] = sunset

        if 'temp' in current_weather:
            current_weather['temp'] = round(current_weather['temp'] - 273.15, 2)
        if 'feels_like' in current_weather:
            current_weather['feels_like'] = round(current_weather['feels_like'] - 273.15, 2)
        if 'dew_point' in current_weather:
            current_weather['dew_point'] = round(current_weather['dew_point'] - 273.15, 2)

        
        return render(request, 'main/news.html', {'articles': articles, 'current_weather': current_weather, 'timezone': timezone})
    else:
        return render(request, 'main/news.html', {'error': 'No se pudo obtener los datos'})