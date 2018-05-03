import requests


def get_weather(city, appid):
    url = "http://samples.openweathermap.org/data/2.5/weather"
    querystring = {"q": city, "appid": appid}
    response = requests.get(url, params=querystring)
    data = response.json()
    return data['weather'][0]['description']


def get_five_days_forecast(city, country_id, appid):
    url = "http://api.openweathermap.org/data/2.5/forecast"
    querystring = {"q": city + ',' + country_id, "appid": appid}
    response = requests.get(url, params=querystring)
    data = response.json()
    forecast = [str(time_dict['dt_txt']) + ' : ' + time_dict['weather'][0]['description'] for time_dict in data['list']]
    return forecast


if __name__ == '__main__':
    pass
