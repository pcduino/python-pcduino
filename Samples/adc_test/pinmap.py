import os.path


class InvalidChannelException(ValueError):
    """The channel sent was invalid."""

    def __init__(self, pin):
        super(InvalidChannelException, self).__init__("pin %s not found" % pin)


class PinMap(object):
    def __init__(self, path, prefix, count):
        self.pins = ['%s%s' % (prefix, i) for i in xrange(count)]
        self.path = path

    def get_path(self, pin, path=None):
        """Get path of pin fd.

        pin can either be the pin basename (i.e. 'adc2') or pin number (i.e. 2)
        if prefix is supplied, override the default path prefix.

        """
        if not path:
            path = self.path

        if isinstance(pin, int):
            try:
                pin = self.pins[pin]
            except IndexError:
                raise InvalidChannelException(pin)

        if not pin in self.pins:
            raise InvalidChannelException(pin)
        return os.path.join(path, pin)
