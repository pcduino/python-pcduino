#!/usr/bin/env python
#
# io test code for pcDuino ( http://www.pcduino.com )
#
from exceptions import InvalidChannelException
__all__ = ['HIGH', 'LOW', 'INPUT', 'OUTPUT','digital_write', 'digital_read',
           "pin_mode"]

_GPIO_PINS = set(('gpio%s' % i for i in xrange(20)))

_PIN_FD_PATH = '/sys/devices/virtual/misc/gpio/pin/%s'
_MODE_FD_PATH = '/sys/devices/virtual/misc/gpio/mode/%s'
HIGH = 1
LOW = 0
INPUT = 0
OUTPUT = 1

def _get_valid_id(channel):
    if channel in _GPIO_PINS:
        return channel
    else:
        raise InvalidChannelException

def digital_write(channel, value):
    """Write to a GPIO channel"""
    id = _get_valid_id(channel)
    with open(_PIN_FD_PATH % id, 'w') as f:
        f.write('1' if value == HIGH else '0')

def digital_read(channel):
    """Read from a GPIO channel"""
    id = _get_valid_id(channel)
    with open(_PIN_FD_PATH % id, 'r') as f:
        return f.read(1) == '1'

def pin_mode(channel, mode):
    """ Set Mode of a GPIO channel """
    id = _get_valid_id(channel)
    with open(_MODE_FD_PATH % id, 'w') as f:
        f.write('0' if mode == INPUT else '1')
