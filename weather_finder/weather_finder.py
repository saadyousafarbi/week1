import requests


API_KEY = '9104e0a25f676b56ac31901d10c5cf0a'
location = 'London'
location_url = ('http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}').format(location, API_KEY)


def get_weather_info(location):
    """
    Gets information about the weather of a location and displays it.

    Arguments:
        location (str): a string that specifies which place to search weather

    """
    weather_raw_data = requests.get(location_url)
    weather_json = weather_raw_data.json()
    if not verify_city(weather_json):
        return None
    else:
        return get_organized_weather_data(weather_json)


def verify_city(json_response):
    """
    Takes in response from OWM and checks if city exists.

    Arguments:
       json_response (json): contains response of a request from OWM

    """
    if json_response['cod'] == '404':
        print('City could not be found, please retry')
        return False

    return True


def get_organized_weather_data(raw_weather_data):
    """
    Gets information about the weather of a location and displays it.

    Arguments:
        raw_weather_data (json): a json object containing all data of location

    """
    organized_data = dict(
        city = raw_weather_data.get('name'),
        country = raw_weather_data.get('sys').get('country'),
        temp = raw_weather_data.get('main').get('temp'),
        temp_max = raw_weather_data.get('main').get('temp_max'),
        temp_min = raw_weather_data.get('main').get('temp_min'),
        humidity = raw_weather_data.get('main').get('humidity'),
        pressure = raw_weather_data.get('main').get('pressure'),
        sky = raw_weather_data['weather'][0]['main'],
        wind = raw_weather_data.get('wind').get('speed'),
        wind_deg = raw_weather_data.get('deg'),
        cloudiness = raw_weather_data.get('clouds').get('all')
    )
    return organized_data


def output_weather_data_on_console(weather_data):
    """
    Prints all the important weather data of the provided place.

    Arguments:
        weather_data (dict): a dictionary containing organized data of weather

    """
    degree_unit = 'F'
    print('---------------------------------------')
    print('Current weather in: {}, {}:'.format(weather_data['city'], weather_data['country']))
    print(weather_data['temp'], degree_unit, weather_data['sky'].encode('ascii'))
    print('Max: {}, Min: {}'.format(weather_data['temp_max'], weather_data['temp_min']))
    print('')
    print('Wind Speed: {}, Degree: {}'.format(weather_data['wind'], weather_data['wind_deg']))
    print('Humidity: {}'.format(weather_data['humidity']))
    print('Cloud: {}'.format(weather_data['cloudiness']))
    print('Pressure: {}'.format(weather_data['pressure']))
    print('---------------------------------------')


output_weather_data_on_console(get_weather_info(location))
