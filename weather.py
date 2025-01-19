import requests

def get_weather(city):
    api_key = "your key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"The weather in {city} is {data['weather'][0]['description']} with a temperature of {data['main']['temp']}°C."
    else:
        return "I couldn't fetch the weather right now. Please try again later."