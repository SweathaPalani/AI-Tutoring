import requests

city_name = "London"
api_key = " "

def get_weather(api_key, city):
    # url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    # response = requests.get(url).json()
    # print(response)
    lat=50
    lon=50
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url).json()
    print(response)


get_weather(api_key, city_name)
