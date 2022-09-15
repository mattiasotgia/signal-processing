
import control
from scipy import signal


__all__ = ['TransferFunction']

class TransferFunction(signal.TransferFunction):
    """Transfer function class

    Parameters
    ----------
    *args:
        Arguments passed to `~scipy.signal.TransferFunction` class.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.gain = None
        self.cutoff = None

    def cutoff():
        """Get cutoff frequency(or frequencies, for second order filters)

        Return
        ------
        cutoff: `float`, `~numpy.ndarray`
            Cutoff frequency for current filter
        """

        # To be implemented

    @property
    def gain(self):
        """Get gain (if active filter, return None otherwise)

        Return
        ------
        gain: `float`, `None`
            Gain for current filter (if active, return `None` otherwise)
        """
        return self._gain

    @gain.setter
    def gain(self, gain):
        """Set gain for current active filter

        Parameters
        ----------
        gain

        Return
        ------
        gain: `float`, `None`
            Gain for current filter (if active, return `None` otherwise)
        """

        if gain < 0:
            raise ValueError("Gain must be greater than Zero, or Zero for passive filters")
        

    