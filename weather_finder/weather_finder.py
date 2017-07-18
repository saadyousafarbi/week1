import requests

API_KEY = '9104e0a25f676b56ac31901d10c5cf0a'


def verify_city(json_response):
    """
    Takes in response from OWM and checks if city exists

    Arguments:
       json_response (json): contains response of a request from OWM
    """

    if json_response['cod'] == '404':
        print 'City could not be found, please retry'
	return False
    else:
	print 'City found'
	return True


def get_weather_info(location):
    """
    Gets information about the weather of a location and displays it

    Arguments:
        location (str): a string that specifies which place to search weather
    """
	
    location_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&APPID=' + API_KEY	
    weather_raw_data = requests.get(location_url)
    weather_json = weather_raw_data.json()
    if not verify_city(weather_json):
	return
    else:
	data_output(data_organizer(weather_json))
 

def data_organizer(weather_raw_data):
    """
    Gets information about the weather of a location and displays it

    Arguments:
        location (str): a string that specifies which place to search weather
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


def data_output(data):
    """
    Prints all the important weather data of the provided place

    Arguments:
        data (dict): a dictionary containing organized data of weather
    """
    m_symbol = 'F'
    print('---------------------------------------')
    print('Current weather in: {}, {}:'.format(data['city'], data['country']))
    print(data['temp'], m_symbol, data['sky'].encode('ascii'))
    print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
    print('')
    print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
    print('Humidity: {}'.format(data['humidity']))
    print('Cloud: {}'.format(data['cloudiness']))
    print('Pressure: {}'.format(data['pressure']))
    print('---------------------------------------')



location = 'London'
get_weather_info(location)
