"""###################################################################################################
# This is a simple script which communicates with OpenWeather API and collect Weather information of Different Cities
####################################################################################################"""
# importing request package to communicate with Web API
import requests
# from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError

# Web URL ('http://api.openweathermap.org/data/2.5/weather?appid=
# Authentication Key= (37a42ce94d4254139d5b57761935c98d)
key = '37a42ce94d4254139d5b57761935c98d'
link = 'http://api.openweathermap.org/data/2.5/weather?appid='+key+'&q='

city_name = raw_input("Enter City Name :")
city_name = city_name or "Islamabad"

# Concatenating web URL and requested City
url = link + city_name

# Getting JSON Data from URL using get methods

try:
    json_data = requests.get(url, timeout=30).json()
except requests.ConnectionError as e:
    print(str(e))
except requests.Timeout as e:
    print(str(e))
except requests.RequestException as e:
    print(str(e))

else:
    # Separating DATA From JSON list and dictionary
    if json_data["cod"] == "404":
        print("City Not Found")
    else:
        weather_condition = json_data["weather"][0]
        temperature = json_data['main']['temp']
        wind_pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind_speed = json_data['wind']['speed']

        # printing Required Data for Output
        print("\nCity Name : " + city_name)
        print("Weather Situation : " + weather_condition['main'])
        print("Temperature : " + str(temperature) + " fahrenheit")
        print("Wind Pressure : " + str(wind_pressure) + " Pascal")
        print("Humidity : " + str(humidity) + " %")
        print("Wind Speed : " + str(wind_speed) + " mph")


