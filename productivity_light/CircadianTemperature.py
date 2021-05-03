import requests
import datetime
from productivity_light.time_to_num import time_to_num as ttn


# Uses IP geolocation API to get local sunrise and sunset times and calculates an ideal light temperature in kelvin
class CircadianTemperature:
    def __init__(self, key):
        self.key = key

    def __get_data(self):
        params = {
            'apiKey': self.key,
        }
        return requests.get('https://api.ipgeolocation.io/astronomy', params=params).json()

    def get_temperature(self, log=False):
        sun_data = self.__get_data()
        sunrise = ttn(datetime.time(int(sun_data['sunrise'][:2]), int(sun_data['sunrise'][3:])))
        sunset = ttn(datetime.time(int(sun_data['sunset'][:2]), int(sun_data['sunset'][3:])))
        current_time = ttn(datetime.datetime.today().time())
        if log: print('sunrise:', sunrise, 'sunset:', sunset, 'current_time:', current_time)

        if current_time < sunrise:
            if log: print('the sun has not risen yet')
            time_until_sunrise = sunrise - current_time
            if time_until_sunrise < 1.5:
                if log: print('it is twilight')
                progress = (1.5 - time_until_sunrise) / 1.5
                temp = 2500 + 5000 * progress
            else:
                if log: print('it is nighttime')
                temp = 2500

        elif current_time < sunset:
            if log: print('the sun has not set yet')
            total_daytime = sunset - sunrise
            time_since_sunrise = current_time - sunrise
            progress = time_since_sunrise / total_daytime
            temp = 7500 - 3000 * progress

        else:
            if log: print('the sun has set already')
            time_since_sunset = current_time - sunset
            if time_since_sunset < 1.5:
                if log: print('it is twilight')
                progress = time_since_sunset / 1.5
                temp = 4500 - 2000 * progress
            else:
                if log: print('it is nighttime')
                temp = 2500

        if log: print(temp)
        return temp
