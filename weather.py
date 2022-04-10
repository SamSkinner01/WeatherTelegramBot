import json
import urllib.request
import key as k

# API and Country Code Needed
API = k.get_weather_api()
country_code = k.get_location()


def get_weather():
    temperatures = []
    search_address = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/" + country_code + "?apikey=" + API + "&details=true"
    # Open URL
    with urllib.request.urlopen(search_address) as search_address:
        data = json.loads(search_address.read().decode())  # Read JSON format
    # Get Values
    temperatures.append(data['DailyForecasts'][0]['Temperature']['Minimum']['Value'])
    temperatures.append(data['DailyForecasts'][0]['Temperature']['Maximum']['Value'])
    return temperatures


