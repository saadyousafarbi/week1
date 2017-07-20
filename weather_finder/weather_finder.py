import requests


API_KEY = '9104e0a25f676b56ac31901d10c5cf0a'
LOCATION = 'London'
WEATHER_API_BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


def get_weather_info(location):
    """
    Gets information about the weather of a location and displays it.

    Arguments:
        location (str): a string that specifies which place to search weather

    """
    location_url = ('{base_url}?q={location}&APPID={app_id}')\
        .format(base_url=WEATHER_API_BASE_URL, location=location, app_id=API_KEY)
    weather_data = requests.get(location_url).json()
    if not verify_city(weather_data):
        return None
    else:
        return get_organized_weather_data(weather_data)


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


def get_organized_weather_data(weather_json):
    """
    Gets information about the weather of a location and displays it.

    Arguments:
        weather_json (json): a json object containing all data of location

    """
    organized_data = dict(
        city = weather_json.get('name'),
        country = weather_json.get('sys').get('country'),
        temp = weather_json.get('main').get('temp'),
        temp_max = weather_json.get('main').get('temp_max'),
        temp_min = weather_json.get('main').get('temp_min'),
        humidity = weather_json.get('main').get('humidity'),
        pressure = weather_json.get('main').get('pressure'),
        sky = weather_json['weather'][0]['main'],
        wind = weather_json.get('wind').get('speed'),
        wind_deg = weather_json.get('deg'),
        cloudiness = weather_json.get('clouds').get('all')
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


organized_weather_data = get_weather_info(LOCATION)
output_weather_data_on_console(organized_weather_data)
