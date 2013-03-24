PWM_IF_PREFIX = "/sys/class/leds/pwm"
PWM_IF_MAX = "max_brightness"
PWM_IF = "brightness"

MAX_PWM_LEVEL = 255

#sprintf(path, "%s%d/%s", PWM_IF_PREFIX, pin, PWM_IF_MAX);

def _max_value(pin):
    return 256

def analog_write(pin, value):
    map_level = (_max_value(pin) * value) / MAX_PWM_LEVEL
    with open("%s%d/%s" % (PWM_IF_PREFIX, pin, PWM_IF), 'w+') as f:
        f.write("%d\n" % map_level)
