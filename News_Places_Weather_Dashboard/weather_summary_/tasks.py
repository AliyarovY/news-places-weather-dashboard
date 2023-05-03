from celery import shared_task
import requests
from .models import WeatherSummary
from place.models import Place

@shared_task
def get_weather_summary():
    places = Place.objects.all()
    for place in places:
        response = requests.get(f'https://api.example.com/weather?city={place.name}')
        data = response.json()
        weather = WeatherSummary(place=place, temperature=data['temperature'], humidity=data['humidity'],
                          pressure=data['pressure'], wind_direction=data['wind_direction'],
                          wind_speed=data['wind_speed'])
        weather.save()

