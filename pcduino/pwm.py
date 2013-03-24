MAX_PWM_NUM = 5
PWM_IF_PREFIX = "/sys/class/leds/pwm"
PWM_IF_MAX = "max_brightness"
PWM_IF = "brightness"

MAX_PWM_LEVEL = 255

def _max_value(pin):
    with open("%s%d/%s" % (PWM_IF_PREFIX, pin, PWM_IF_MAX)) as f:
        return int(f.read())

def analog_write(pin, value):
    if (pin < 0 or pin > MAX_PWM_NUM or
        value < 0 or value > MAX_PWM_LEVEL):
        raise ValueError(
            "pin must be between 0 and %s. value must be between 0 and %s" % (
                MAX_PWM_NUM, MAX_PWM_LEVEL))

    map_level = (_max_value(pin) * value) / MAX_PWM_LEVEL
    with open("%s%d/%s" % (PWM_IF_PREFIX, pin, PWM_IF), 'w+') as f:
        f.write("%d\n" % map_level)
