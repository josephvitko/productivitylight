import datetime
import requests
from pprint import pprint


class RescueTime_API:
    def __init__(self, key):
        self.key = key

    def get_time_data(self, day):
        payload = {'key': self.key,
                   'perspective': 'interval',
                   'restrict_kind': 'productivity',
                   'interval': 'day',
                   'restrict_begin': str(day),
                   'restrict_end': str(day),
                   'format': 'json'
                   }
        print(payload)  # for debugging
        response = requests.get('https://www.rescuetime.com/anapi/data', params=payload)
        data = response.json().get('rows')
        print(data)  # for debugging
        day_prods = [0, 0, 0, 0, 0]
        for row in data:
            level = row[3]
            day_prods[level + 2] = row[1] / 3600.0
        return day_prods

    def get_net_productivity(self, day):
        data = self.get_time_data(day)
        semi_factor = 0.5
        productive_time = data[4] + data[3] * semi_factor
        unproductive_time = data[0] + data[1] * semi_factor
        return productive_time - unproductive_time



