import numpy as np
import awkward as ak

from uncertainties import ufloat, unumpy

class DataReader:
    """Read data from file and format accordingly

    Parametets
    ----------
    file : `string`, `None`
        The filename for the data set, in any format
    format: `string`, default `None`
        The format in wich the data set is written
        Possible choices are `None`, 'csv' (the data headers are used 
        to infere the values), or 'xlsx' (same as 'csv').

    Return
    ------
    DataReader
    """
    def __init__(self, file = None, format=None) -> None:
        self.__file = open(file)

        if format is 'csv':
            pass
    
    def magnitude()
    """Get magnitude array (real values) from data

    """