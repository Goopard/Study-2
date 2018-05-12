"""
This module contains the functions used to get the current weather and weather forecasts using openweathermap.org and
Nominatim APIs.
"""

import requests
import sys


def get_coordinates(address):
    """This function finds out the coordinates by address using the Nominatim API.

    :param address: Address.
    :type address: list.
    :return: tuple(float) -- the required coordinates.
    """
    url = 'https://nominatim.openstreetmap.org/search?q={}&format=json'.format(address)
    response = requests.get(url)
    data = response.json()
    try:
        lat = data[0]['lat']
        lon = data[0]['lon']
    except IndexError:
        print('Wrong address!')
        sys.exit()
    return lat, lon


def get_weather(address, appid):
    """This function finds out the current weather for some given address using openweather.org API.

    :param address: Address.
    :type address: list.
    :param appid: APPID used by the openweathermap.org API.
    :type appid: str.
    :return: list -- the required weather data.
    """
    lat, lon = get_coordinates(address)
    url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'.format(lat, lon, appid)
    response = requests.get(url)
    data = response.json()
    return data


def get_five_day_forecast(address, appid):
    """This function finds out the 5-day weather forecast for some given address using openweather.org API.

    :param address: Address.
    :type address: list.
    :param appid: APPID used by the openweathermap.org API.
    :type appid: str.
    :return: dict -- the required weather data.
    """
    lat, lon = get_coordinates(address)
    url = 'http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid={}'.format(lat, lon, appid)
    response = requests.get(url)
    data = response.json()['list']
    forecast = {time['dt_txt']: [time['weather'][0]['description'],
                                 round(time['main']['temp'] - 274),
                                 round(time['main']['pressure'] * 0.750062),
                                 time['main']['humidity'],
                                 time['wind']['speed']] for time in data}
    return forecast


def print_weather(address, appid):
    """This function prints the data returned by the function get_weather in a nice way.

    :param address: Address.
    :type address: list.
    :param appid: APPID used by the openweathermap.org API.
    :type appid: str.
    """
    weather = get_weather(address, appid)
    address_str = ''
    for comp in address:
        address_str += comp + ' '
    print('Current weather in {}:'.format(address_str))
    print('Sky: {}'.format(weather['weather'][0]['description']))
    print('Temperature: {} °C'.format(round(weather['main']['temp'] - 274)))
    print('Pressure: {} mm Hg'.format(round(weather['main']['pressure'] * 0.750062)))
    print('Humidity: {}%'.format(weather['main']['humidity']))
    print('Wind speed: {} m/s'.format(weather['wind']['speed']))


def normalized(value, length):
    """This function is used to cast the variable value to the str format and add some whitespaces to it so that its
    length will be equal to argument length.

    :param value: Given variable.
    :type value: any.
    :param length: The length of the returned str.
    :type length: int.
    :return: str -- the required str of length length.
    """
    res = str(value)
    while len(res) < length:
        res += ' '
    return res


def print_forecast(address, appid):
    """This function prints the data returned by the function get_five_day_forecast in a nice way (as a table).

    :param address: Address.
    :type address: list.
    :param appid: APPID used by the openweathermap.org API.
    :type appid: str.
    """
    forecast = get_five_day_forecast(address, appid)
    address_str = ''
    for comp in address:
        address_str += comp + ' '
    print('5-day forecast for {}:'.format(address_str))
    print(normalized('   Date and time', 20),
          normalized('   Sky', 10),
          normalized('Temperature', 12),
          normalized('Pressure', 10),
          normalized('Humidity', 10),
          normalized('Wind speed', 15))
    for time in forecast:
        print(normalized(time, 20),
              normalized(forecast[time][0], 10),
              normalized('   ' + str(forecast[time][1]) + '°C', 12),
              normalized(str(forecast[time][2]) + ' mm Hg', 10),
              normalized('  ' + str(forecast[time][3]) + '%', 10),
              normalized(' ' + str(forecast[time][4]) + ' m/s', 15))
