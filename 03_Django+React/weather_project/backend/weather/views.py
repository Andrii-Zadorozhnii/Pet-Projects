import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view

# API-ключ OpenWeather (замени на свой)
API_KEY = "fb4be141d3227cd5f949355455e38556"


@api_view(['GET'])
def get_weather(request):
    """Получает погоду по названию города."""
    city = request.GET.get('city', 'London')  # Получаем город из запроса
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return Response({"error": "Город не найден"}, status=404)

    weather_data = {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png"
    }

    return Response(weather_data)