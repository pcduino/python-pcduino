import os.path
from os import listdir

MAX_PWM_LEVEL = 255

def analog_write(pin, value):
    """Write to one of the pwm pins.

    value can be an number between 0 and 255.

    """

    path = '/sys/class/misc/pwmtimer/'

    ending = 'pwm' + str(pin)

    pins = listdir(os.path.join(path, 'enable'))
    if not ending in pins:
        raise ValueError("Pin not found, PWM only possible on " + " ".join(str(p) for p in pins) + ".")

    with open(os.path.join(path, 'max_level',ending)) as f:
        max_value = int(f.read())

    if value < 0 or value > MAX_PWM_LEVEL:
        raise ValueError("value must be between 0 and %s" % MAX_PWM_LEVEL)

    map_level = ((max_value-1) * value) // MAX_PWM_LEVEL
   	#-1 because if it puts max_value the duty cycle somehow becomes 0 (overflow)

    #disable -> change level -> enable , as requested by documentation
    with open(os.path.join(path, 'enable', ending), 'w+') as f:
        f.write("0\n")

    with open(os.path.join(path, 'level', ending), 'w+') as f:
        f.write("%d\n" % map_level)

    with open(os.path.join(path, 'enable', ending), 'w+') as f:
        f.write("1\n")
