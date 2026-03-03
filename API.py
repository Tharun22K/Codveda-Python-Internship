import requests

city = input("Enter city name: ")
api_key = "480c38e700738dd60d1a8a9c8afffbfd"  # Replace with your OpenWeather API key

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["description"])
else:
    print("Error fetching data!")
