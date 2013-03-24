_ADC_PREFIX = '/proc/adc'
_N_PINS= 6


def analogRead(channel):
    with open(_ADC_PREFIX % id, 'r') as f:
        return f.read(1)
