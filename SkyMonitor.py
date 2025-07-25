import requests
import time
import matplotlib.pyplot as plt

api_key="c98b496f91d94756a48395bc3f63f2e1"
city = input("city name :")
url = f'https://api.weatherbit.io/v2.0/current?city={city}&key={api_key}&units=M'

temps= []
humidities =[]
times = []

for i in range(1):
    response = requests.get(url)
    data = response.json()
    temp= data['data'][0]['temp']
    humidity = data['data'][0]['rh']
    temps.append(temp)
    humidities.append(humidity)
    times.append(i)

    if temp > 25:
        x = "the weather is gharmeee"
    elif 15 <= temp <= 25 :
        x = "the weather is bad nist"
    else:
        x = "the weather is sarde"

    if humidity > 70:
        plant_cover_status = "Good plant growth expected."
    elif 40 <= humidity <= 70:
        plant_cover_status = "Moderate plant growth."
    else:
        plant_cover_status = "Poor plant growth."

    print(f"Time {i}: Temperature = {temp}°C -> {x}")
    print(f"Humidity = {humidity}% -> {plant_cover_status}")
