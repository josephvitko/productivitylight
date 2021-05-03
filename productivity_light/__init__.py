from productivity_light.LIFX_API import LIFX_API
from productivity_light.RescueTime_API import RescueTime_API
from productivity_light.CircadianTemperature import CircadianTemperature
from productivity_light.Logging_API import Logging_API
import time
import datetime


# main function to run productivity light
#
# lifx_token: LIFX API token, required
# rt_token: RescueTime API token, required
# scale: number of hours of net productive/distracting time for the light color to reach max saturation, default 10
# prod_hue: hue (in degrees) of the light's color when net daily productivity is positive, default 137 (blue)
# dist_hue: hue (in degrees) of the light's color when net daily productivity is negative, default 0 (red)
# cycle_length: length in seconds of how often the light color should be updated, default 300
# light_index: the index of the light to use (you may need to experiment with this in multi-light setups), default 0
# circadian: True/False option to change light temperature based on time of day, default False
# ct_token: http://ipgeolocation.io API token needed to get sunrise/sunset times for optional circadian feature
# debug: True/False option to display debug info in console, default False
# log_url: optional url to send RescueTime data to log on a personal server
def productivity_light(lifx_token, rt_token, circadian=False, ct_token=None,
                       log_url=None, debug=False, scale=10, prod_hue=137, dist_hue=0,
                       light_index=0, cycle_length=300):
    while True:
        # create API wrapper objects
        lifx_api = LIFX_API(token=lifx_token)
        rt_api = RescueTime_API(rt_token)
        ct_api = CircadianTemperature(ct_token)

        #
        light = lifx_api.list_lights()[light_index]
        net_productivity = rt_api.get_net_productivity()  # in hours
        if log_url is not None:
            # send productivity data to be logged
            try:
                log_api = Logging_API(log_url)
                log_api.send_data(prod_hours=rt_api.productive_time,
                                  dist_hours=rt_api.unproductive_time,
                                  date=datetime.datetime.today().date())
            except:
                print('could not log data')
        strength = abs(net_productivity / scale)

        if circadian:
            temp = ct_api.get_temperature(log=debug)  # in kelvin
        else:
            temp = light.color.kelvin

        if net_productivity < 0:
            light.modify_color(hue=dist_hue, saturation=strength, kelvin=temp)
        else:
            light.modify_color(hue=prod_hue, saturation=strength, kelvin=temp)
        if debug: print(str(datetime.datetime.today()) + ", netp: " +
                        str(round(net_productivity, 1)) + ', ' + str(light.color))
        time.sleep(cycle_length)
