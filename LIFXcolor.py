from Light import Light


class LIFXcolor:
    def __init__(self, hue, saturation, brightness, kelvin):
        self.hue = self.__set_hue(hue)
        self.saturation = self.__set_saturation(saturation)
        self.brightness = self.__set_brightness(brightness)
        self.kelvin = self.__set_kelvin(kelvin)

    def set(self, caller, hue=None, saturation=None, brightness=None, kelvin=None):
        if not isinstance(caller, Light):
            raise TypeError('Light color cannot be modified directly')
        if hue is None: hue = self.hue
        if saturation is None: saturation = self.saturation
        if brightness is None: brightness = self.brightness
        if kelvin is None: kelvin = self.kelvin

        self.__set_hue(hue)
        self.__set_saturation(saturation)
        self.__set_brightness(brightness)
        self.__set_kelvin(kelvin)

    def __set_hue(self, hue):
        if not 359 >= hue >= 0:
            raise ValueError('Warning: Hue is not in range')
        self.hue = hue

    def __set_saturation(self, saturation):
        if not 1.0 >= saturation >= 0.0:
            raise ValueError('Warning: saturation is not in range')
        self.saturation = saturation

    def __set_brightness(self, brightness):
        if not 1.0 >= brightness >= 0.0:
            raise ValueError('Warning: brightness is not in range')
        self.brightness = brightness

    def __set_kelvin(self, kelvin):
        if not 9000 >= kelvin >= 2000:
            raise ValueError('Warning: kelvin is not in range')
        self.kelvin = kelvin

    def __to_string(self):
        s = "hue:" + str(self.hue) + \
            " saturation:" + str(self.saturation) + \
            " brightness:" + str(self.brightness) + \
            " kelvin:" + str(self.kelvin)
        return s

# c = LIFXcolor(0, 0.5, 0.5, 6000)
# print(c.to_string())
# c.validate()
