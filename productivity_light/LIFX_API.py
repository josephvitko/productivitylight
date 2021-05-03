import requests
from productivity_light.LIFXcolor import LIFXcolor
from productivity_light.Light import Light


# LIFX API wrapper
class LIFX_API:
    # constructor that requires LIFX API token
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": "Bearer %s" % token}

    # returns a list of Light objects for each of the user's LIFX lights
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

    # sets a LIFX light with a particular label to a specified state
    def set_state(self, label, state, value):
        payload = {
            state: value
        }
        requests.put('https://api.lifx.com/v1/lights/label:' + label + '/state',
                     headers=self.headers,
                     data=payload)

    # validates that a color string is in a format that the LIFX API can understand
    def validate_color(self, color_string):
        response = requests.get('https://api.lifx.com/v1/color', params={'string': color_string}, headers=self.headers)
        print(response.text)
