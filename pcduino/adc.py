from exceptions import InvalidChannelException
import os.path

_ADC_PREFIX = '/proc'
_N_PINS= 6
_ADC_PINS = set(('adc%s' % i for i in xrange(_N_PINS)))


def _get_path(id_):
    if id_ in _ADC_PINS:
        return os.path.join(_ADC_PREFIX, id_)
    raise InvalidChannelException

def analog_read(channel):
    with open(_get_path(channel), 'r') as f:
        return int(f.read(32).split(':')[1].strip())
