class AlphaFilter:
    _alpha = 0.2
    _SPEED_ACCEL_LIMIT = 19.05

    def __init__(self, x=0):
        self.x = x

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, alpha):
        '''
        Set alpha parameter. The alpha parameter should be non-zero
        positive less than one. If an out of range value is assigned,
        the value is forced to 0.1 or 1.
        '''
        try:
            assert (alpha > 0) and (alpha < 1)
        except AssertionError:
            print('Warning: alpha should non-zero positive and < 1.\
            alpha forced to 0.1 or 1.')

        if alpha < 0:
            self._alpha = 0.1
        elif alpha > 1:
            self._alpha = 1
        else:
            self._alpha = alpha

    def filter(self, z):
        """
        Update prediction using current measurement z
        """
        delta_x = z - self.x  # residue
        self.x = self.x + self._alpha*delta_x
