import requests
from LIFXcolor import LIFXcolor
from Light import Light


class LIFX_API:
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": "Bearer %s" % token}

    def list_lights(self):
        response = requests.get('https://api.lifx.com/v1/lights/all', headers=self.headers)
        lights_dict = response.json()
        lights = []
        for li in lights_dict:
            c = li.get('color')
            color = LIFXcolor(hue=c.get('hue'),
                              saturation=c.get('saturation'),
                              kelvin=c.get('kelvin'),
                              brightness=li.get('brightness'))
            light = Light(label=li.get('label'),
                          power=li.get('power'),
                          color=color,
                          api=self)
            lights.append(light)
        return lights

    def set_state(self, label, state, value):
        payload = {
            state: value
        }
        requests.put('https://api.lifx.com/v1/lights/label:' + label + '/state',
                     headers=self.headers,
                     data=payload)

    def validate_color(self, color_string):
        response = requests.get('https://api.lifx.com/v1/color', params={'string': color_string}, headers=self.headers)
        print(response.text)
