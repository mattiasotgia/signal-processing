'''General TransferFunction class

'''

import control
from scipy import signal

class TransferFunction(control.TransferFunction):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    