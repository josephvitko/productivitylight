from productivity_light.LIFXcolor import LIFXcolor


# Represents an LIFX light and is controlled using an LIFX_API object
class Light:
    def __init__(self, api, label, power, color):
        self.api = api  # LIFX_API object
        self.label = label
        self.power = power
        self.color = color

    # Turns a light "on" or "off"
    def set_power(self, state):
        if state != "on" and state != "off":
            raise ValueError("Error: desired state is not on or off")
        self.power = state
        self.api.set_state(self.label, "power", state)

    # Toggles the light's power state between "on" and "off"
    def flip_power(self):
        if self.power == "on":
            self.set_power("off")
        else:
            self.set_power("on")

    # Sets the light's color using an LIFXcolor object
    def set_color(self, color):
        if not isinstance(color, LIFXcolor):
            raise TypeError('color must be set to an LIFXcolor')
        self.color = color
        self.update_color()

    # Set color of physical light to value of class property, communicating using the LIFX_API object
    def update_color(self):
        self.api.set_state(self.label, "color", str(self.color))

    # Modifies specified color properties by interacting with existing LIFXcolor rather than creating new one
    def modify_color(self, hue=None, saturation=None, brightness=None, kelvin=None):
        if hue is None: hue = self.color.hue
        if saturation is None: saturation = self.color.saturation
        if brightness is None: brightness = self.color.brightness
        if kelvin is None: kelvin = self.color.kelvin
        self.color.set(hue, saturation, brightness, kelvin, self)
        self.update_color()

    # Returns string representation of light
    def __str__(self):
        return self.label + ', ' + self.power + ', ' + str(self.color)
