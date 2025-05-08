import requests # pip install requests

api_key = "your_api_key"
city = input("Enter your city: ")

response = requests.get(f"http://api.openweathermap.org/data/3.0/weather?q={city}&appid={api_key}")
weather_data = response.json()

print (f"{weather_data}")   

print(f"Weather in {city}: {weather_data['weather'][0]['description']}")