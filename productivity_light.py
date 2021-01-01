from LIFX_API import LIFX_API
from RescueTime_API import RescueTime_API
from CircadianTemperature import CircadianTemperature
import time
import datetime


def productivity_light(lifx_token, rt_token, ct_token='', log=False, circadian=True):
    while True:
        api = LIFX_API(token=lifx_token)
        rt_api = RescueTime_API(rt_token)
        ct_api = CircadianTemperature(ct_token)

        light = api.list_lights()[0]
        net_productivity = rt_api.get_net_productivity_today()  # in hours
        scale = 10  # hours for max effect
        strength = abs(net_productivity / scale)

        if circadian:
            temp = ct_api.get_temperature(log=log)  # in kelvin
        else:
            temp = light.color.kelvin

        if net_productivity < 0:
            light.modify_color(hue=0, saturation=strength, kelvin=temp)
        else:
            light.modify_color(hue=137, saturation=strength, kelvin=temp)
        if log: print(str(datetime.datetime.today()) + ", " + str(light.color))
        time.sleep(300)
