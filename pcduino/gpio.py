from pinmap import PinMap


__all__ = ['HIGH', 'LOW', 'INPUT', 'OUTPUT','digital_write', 'digital_read',
           "pin_mode"]

HIGH = 1
LOW = 0
INPUT = 0
OUTPUT = 1

gpio_pins = PinMap(
    '/sys/devices/virtual/misc/gpio/pin',
    'gpio',
    20
)

gpio_mode_pins = PinMap(
    '/sys/devices/virtual/misc/gpio/mode/',
    'gpio',
    20
)

def digital_write(channel, value):
    """Write to a GPIO channel"""
    path = gpio_pins.get_path(channel)
    with open(path, 'w') as f:
        f.write('1' if value == HIGH else '0')

def digital_read(channel):
    """Read from a GPIO channel"""
    path = gpio_pins.get_path(channel)
    with open(path, 'r') as f:
        return f.read(1) == '1'

def pin_mode(channel, mode):
    """ Set Mode of a GPIO channel """
    path = gpio_mode_pins.get_path(channel)
    with open(path, 'w+') as f:
        f.write('0' if mode == INPUT else '1')
