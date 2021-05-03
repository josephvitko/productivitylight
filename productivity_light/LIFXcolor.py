# Represents the properties of an LIFX light, including hue, saturation, brightness, and kelvin (temperature)
# This object should only be modified by a Light object, as direct modification would not adjust physical LIFX light
class LIFXcolor:
    def __init__(self, hue, saturation, brightness, kelvin):
        self.hue = self.__set_hue(hue)
        self.saturation = self.__set_saturation(saturation)
        self.brightness = self.__set_brightness(brightness)
        self.kelvin = self.__set_kelvin(kelvin)

    def set(self, hue=None, saturation=None, brightness=None, kelvin=None, caller=None,):
        if not caller:
            # TODO: ensure caller is of type Light without circular importing
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
        return hue

    def __set_saturation(self, saturation):
        if not 1.0 >= saturation >= 0.0:
            raise ValueError('Warning: saturation is not in range')
        self.saturation = saturation
        return saturation

    def __set_brightness(self, brightness):
        if not 1.0 >= brightness >= 0.0:
            raise ValueError('Warning: brightness is not in range')
        self.brightness = brightness
        return brightness

    def __set_kelvin(self, kelvin):
        if not 9000 >= kelvin >= 2000:
            raise ValueError('Warning: kelvin is not in range')
        self.kelvin = int(kelvin)
        return kelvin

    def __str__(self):
        s = "hue:" + str(self.hue) + \
            " saturation:" + str(self.saturation) + \
            " brightness:" + str(self.brightness) + \
            " kelvin:" + str(self.kelvin)
        return s

