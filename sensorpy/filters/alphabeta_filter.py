"""
This module is a part of the sensorpy package.

Saurav R. Tuladhar (@sauravrt)
"""

class AlphaFilter:
    """
    AlphaFilter class implements the Alpha filter.
    """
    _alpha = 0.2

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

# =============================================================================

class AlphaBetaFilter:
    """
    Implements Alpha-Beta filter
    """
    _alpha = 0.75
    _beta = _alpha**2/(2 - _alpha) 

    def __init__(self, x=0):
        '''
        Initialize alpha-beta filter. Initial value x defaults to zero, but it
        can be set appropriately for particular application. delta_t can also
        be set at each update step.
        '''
        self.x = x
        self.rate_x = 0
        self.dt = 1
    
    @property
    def alpha(self):
        return self._alpha

    @property
    def beta(self):
        return self._beta

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

        self._beta = alpha**2/(2 - alpha)


    def filter(self, z):
        '''
        Alpha-beta filtering
        '''
        pred = self.x + self.dt*self.rate_x
        residual = z - pred
        self.x = pred + self._alpha*residual
        self.rate_x = self.rate_x + self._beta*residual/self.dt
        

