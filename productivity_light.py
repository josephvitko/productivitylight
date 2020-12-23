from LIFX_API import LIFX_API
from RescueTime_API import RescueTime_API
import time
import datetime


def productivity_light(lifx_token, rt_token, log=False):
    while True:
        api = LIFX_API(token=lifx_token)
        rt_api = RescueTime_API(rt_token)

        light = api.list_lights()[0]
        net_productivity = rt_api.get_net_productivity_today()  # in hours
        scale = 10  # hours for max effect
        strength = abs(net_productivity / scale)

        if net_productivity < 0:
            light.modify_color(hue=0, saturation=strength)
        else:
            light.modify_color(hue=210, saturation=strength)
        if log: print(str(datetime.datetime.today()) + ", netP:" + str(round(net_productivity, 1)) + ", " + str(light.color))
        time.sleep(300)
