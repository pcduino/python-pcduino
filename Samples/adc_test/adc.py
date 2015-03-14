from pinmap import PinMap

pins = PinMap('/proc', 'adc', 6)

def analog_read(channel):
    """Return the integer value of an adc pin.

    adc0 and adc1 have 6 bit resolution.
    adc2 through adc5 have 12 bit resolution.

    """
    with open(pins.get_path(channel), 'r') as f:
        return int(f.read(32).split(':')[1].strip())
