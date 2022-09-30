import numpy
from uncertainties import ufloat, unumpy

class FrequencySeries:
    """Frequency series base constructor

    Parameters
    ----------
    data : `tfpy.reader.DataReader`
        The full data in complex space format

    rad : `bool`, optional, default: `True`
        Set if the phase data/fit needs to be formatted as radians
    dB : `bool`, optional, default: `True`
        if `True`, display magnitude in decibels, otherwise display
        amplitude.


    Returns
    -------
    filter `FrequncySeries`

    """

    def __init__(self,**kwargs):
        """Base constructor for 
        `tfpy.frequencyseries.FrequencySeries` class
        """

        self.rad = kwargs.pop('rad', True)
        self.dB = kwargs.pop('dB', True)

    
    def _type(self):
        """"Return the type (Magnitude/amplitude, Phase) dict for labeling"""
        _type = dict()
        _type['phase'] = 'Phase'
        if self.dB:
            _type['magnitude'] = 'Magnitude'
            return _type
        else:
            _type['magnitude'] = 'Amplitude'
            return _type

    def data():
        """
        Return the full data array for plotting
        or future data analysis
        """

        return _data

    def fit(npoints=1000):
        """
        Return the full fit array for plotting
        
        Parameters
        ----------
        npoints : 

        Return
        ------
        fit : `dict(ndarray)`, or `None` if failed
            default shape is (N=1000, 1) for each array
        """

# class ComplexFunction:

#     def __init__(self, data):
        
#         self._frequencies = None
#         self._magnitude = None
#         self._phase = None

#     def frequencies(self):
#         """Return complex function magnitude"""
#         return self._frequencies

#     @frequencies.setter
#     def frequencies(self, frequencies):
#         """Return complex function magnitude"""
#         return self._magnitude
# 
#     def magnitude(self):
#         """Return complex function magnitude"""
#         return self._magnitude
    
#     def magnitude(self):
#         """Return complex function phase"""
#         return self._phase
    
