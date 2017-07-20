import requests

API_KEY = '9104e0a25f676b56ac31901d10c5cf0a'


def get_weather_info(location):
    """
    Gets information about the weather of a location and displays it.

    Arguments:
        location (str): a string that specifies which place to search weather
    """
    location_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&APPID=' + API_KEY
    weather_raw_data = requests.get(location_url)
    weather_json = weather_raw_data.json()
    if not verify_city(weather_json):
        return
    else:
        weather_data_output_on_console(weather_data_organizer(weather_json))


def verify_city(json_response):
    """
    Takes in response from OWM and checks if city exists.

    Arguments:
       json_response (json): contains response of a request from OWM
    """
    if json_response['cod'] == '404':
        print('City could not be found, please retry')
        return False

    print('City found')
    return True


def weather_data_organizer(weather_raw_data):
    """
    Gets information about the weather of a location and displays it.

    Arguments:
        weather_raw_data (json): a json object containing all data of location
    """
    organized_data = dict(
        city = weather_raw_data.get('name'),
        country = weather_raw_data.get('sys').get('country'),
        temp = weather_raw_data.get('main').get('temp'),
        temp_max = weather_raw_data.get('main').get('temp_max'),
        temp_min = weather_raw_data.get('main').get('temp_min'),
        humidity = weather_raw_data.get('main').get('humidity'),
        pressure = weather_raw_data.get('main').get('pressure'),
        sky = weather_raw_data['weather'][0]['main'],
        wind = weather_raw_data.get('wind').get('speed'),
        wind_deg = weather_raw_data.get('deg'),
        cloudiness = weather_raw_data.get('clouds').get('all')
    )
    return organized_data


def weather_data_output_on_console(weather_data):
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


location = 'London'
get_weather_info(location)
