from LIFXcolor import LIFXcolor


class Light:
    def __init__(self, api, label, power, color):
        self.api = api
        self.label = label
        self.power = power
        self.color = color

    def set_power(self, state):
        if state != "on" and state != "off":
            raise ValueError("Error: desired state is not on or off")
        self.power = state
        self.api.set_state(self.label, "power", state)

    def flip_power(self):
        if self.power == "on":
            self.set_power("off")
        else:
            self.set_power("on")

    def set_color(self, color):
        if not isinstance(color, LIFXcolor):
            raise TypeError('color must be set to an LIFXcolor')
        self.color = color
        self.update_color()

    def update_color(self):
        self.api.set_state(self.label, "color", str(self.color))

    def modify_color(self, hue=None, saturation=None, brightness=None, kelvin=None):
        if not hue: hue = self.color.hue
        if not saturation: saturation = self.color.saturation
        if not brightness: brightness = self.color.brightness
        if not kelvin: kelvin = self.color.kelvin
        self.color.set(hue, saturation, brightness, kelvin, self)
        self.update_color()

    def __str__(self):
        return self.label + ', ' + self.power + ', ' + str(self.color)
