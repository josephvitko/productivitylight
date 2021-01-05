import requests


class Logging_API:
    def __init__(self, url):
        self.url = url

    def send_data(self, prod_hours, dist_hours, date):
        data = {
            'date': date,
            'prod_hours': prod_hours,
            'dist_hours': dist_hours,
        }
        response = requests.post(self.url, data=data)