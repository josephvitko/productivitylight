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
                   'restrict_begin': day,
                   'restrict_end': day,
                   'format': 'json'
                   }
        response = requests.get('https://www.rescuetime.com/anapi/data', params=payload)
        data = response.json().get('rows')
        day_prods = [0, 0, 0, 0, 0]
        for row in data:
            level = row[3]
            day_prods[level + 2] = row[1] / 3600.0
        return day_prods

    def get_net_productivity_today(self):
        day = str(datetime.datetime.today())[:10]
        data = self.get_time_data(day)
        semi_factor = 0.5
        productive_time = data[4] + data[3] * semi_factor
        unproductive_time = data[0] + data[1] * semi_factor
        return productive_time - unproductive_time



