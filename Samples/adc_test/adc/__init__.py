#!/usr/bin/env python

_PIN_FD_PATH = '/proc/adc%s'


def analog_read(channel):
    """Return the integer value of an adc pin.

    adc0 and adc1 have 6 bit resolution.
    adc2 through adc5 have 12 bit resolution.

    """


    with open(_PIN_FD_PATH % channel, 'r') as f:
        return int(f.read(32).split(':')[1].strip())