import os.path

from pinmap import PinMap


pins = PinMap('/sys/class/leds', 'pwm', 5)

MAX_PWM_LEVEL = 255

def analog_write(pin, value):
    """Write to one of the pwm pins.

    value can be an number between 0 and 255.

    """
    path = pins.get_path(pin)

    with open(os.path.join(path, 'max_brightness')) as f:
        max_value = int(f.read())

    if value < 0 or value > MAX_PWM_LEVEL:
        raise ValueError(
            "pin must be between 0 and %s. value must be between 0 and %s" % (
                MAX_PWM_NUM, MAX_PWM_LEVEL))

    map_level = (max_value * value) / MAX_PWM_LEVEL
    with open(os.path.join(path, 'brightness'), 'w+') as f:
        f.write("%d\n" % map_level)
