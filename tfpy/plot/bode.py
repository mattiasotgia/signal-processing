from matplotlib import figure
import numpy


def to_db(a):  # pylint: disable=invalid-name
    """Convert the input array into decibels

    Parameters
    ----------
    a : `float`, `numpy.ndarray`
        value or array of values to convert to decibels

    Returns
    -------
    dB : ``10 * numpy.log10(a)``

    Examples
    --------
    >>> to_db(1000)
    30.0
    """
    return 10 * numpy.log10(a)

def to_db_err(a, err_a):  # pylint: disable=invalid-name
    """Convert the input array into decibels

    Parameters
    ----------
    a : `float`, `numpy.ndarray`
        value or array of values to convert to decibels
    err_a : `float`, `numpy.ndarray`
        value or array of uncertainties to convert to decibels

    Returns
    -------
    err_dB : ``err(10 * numpy.log10(a))``
    """
    return 10 * err_a / ( a * np.log(10) )


class Bode(figure.Figure):
    """A `Plot` class for visualising transfer functions
    
    Parameters
    ----------
    *filters : `tfpy.[??]` #TODO!
        

    split : `bool`, optional, default: `True`
        if `True`, display magnitude an phase plots as separate axes,
        otherwise display them in a single axis.
    rad : `bool`, optional, default: `True`
        if `True`, display phase in radians, otherwise display
        in degrees.
    dB : `bool`, optional, default: `True`
        if `True`, display magnitude in decibels, otherwise display
        amplitude.

    Returns
    -------
    plot : `BodePlot`
        a new BodePlot with two `Axes` - :attr:`~BodePlot.maxes` and
        :attr:`~BodePlot.paxes` - representing the magnitude and
        phase of the input transfer function(s) respectively.
    """

    def __init__(self, *filters, **kwargs):
        """Initialize BodePlot class object
        """
        dB = kwargs.pop('dB', True)
        rad = kwargs.pop('rad',True)
        split = kwargs.pop('split', True)

        # parse plotting arguments
        figargs = dict()
        title = kwargs.pop('title', None)
        for key in ['figsize', 'dpi', 'frameon', 'subplotpars',
                    'tight_layout']:
            if key in kwargs:
                figargs[key] = kwargs.pop(key)

        # generate figure
        super().__init__(**figargs)

        if split:
            figargs.setdefault('figsize',(12,5))
            # delete the axes, and create two more
            self.add_subplot(1, 2, 1)
            self.add_subplot(1, 2, 2)
        else:
            pass # TODO: implement non-split version

        if dB:
            self.maxes.set_ylabel('Magnitude (dB)')
            ylim = self.maxes.get_ylim()
            # if ylim[1] == 0:
            #     self.maxes.set_ybound(
            #         upper=ylim[1] + (ylim[1] - ylim[0]) * 0.1)
        else:
            self.maxes.set_yscale('log')
            self.maxes.set_ylabel('Amplitude')
        if rad:
            self.paxes.set_ylabel('Phase (rad)')
        else:
            self.paxes.set_ylabel('Phase (deg)')

        self.paxes.set_xlabel('Frequency (Hz)')
        self.maxes.set_xscale('log')
        self.paxes.set_xscale('log')

    
    @property
    def maxes(self):
        """`FrequencySeriesAxes` for the Bode magnitude
        """
        return self.axes[0]

    @property
    def paxes(self):
        """`FrequencySeriesAxes` for the Bode phase
        """
        return self.axes[1]

