# Productivity Light
A Python library that automatically sets the color of an LIFX light based on your RescueTime productivity.

This library communicates with your light using the LIFX API and gets your daily productivity using the RescueTime API. You will need a key from both of these services.

You can also use the optional "Circadian" mode. With this enabled, the Kelvin temperature of your LIFX light will change throughout the day to correlate with natural light. Your local sunrise and sunset times are retreived using ipgeolocation.io's free astronomy API, so you will need a key to use this feature.

## How it works
First, your net-productivity in hours is calculated by subtracting your distracting time today from your productive time. The semi-productive/distracting time is weighted only 50%

Your light's hue will then bet set depending on if this value is positive or negative. By default, green indicates more productive time than distracting time while red indicates the opposite.

The saturation of this color is calculated by dividing your net-productivity by a scale factor. This factor is preset to 10 hours, but can be configured (as can your choices for hues). So, if you had 8 productive hours today and 3 unproductive hours, your light would be green with a saturation of 50%. If net-productivity is 0, the color will simply be white. 

The human body's work and sleep schedule naturally follows changes in sunlight, especially changes in blue light exposure throughout the day. Circadian mode mimics these changes by adjusting the light's temperature to be warmer or bluer based on the time.

At night, the light will be a warm 2500K, similar to a candle. Beginning an hour and a half before sunrise, the temperature will gradually cool until it reaches a peak of 7500K at sunrise. During daytime, the temperature will slowly decrease back to 4500K at sunset. From there, the temperature will quickly warm to the night temperature over the following hour and a half of twilight.

Overall, these changes in color and temperature are meant to promote a healthy and productive schedule.

## Usage
Implementing the main functionality of Productivity Light is easy:
    productivity_light(lifx_token={insert lifx api key here}, rt_token={inset rescuetime api key here})
