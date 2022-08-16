import sys
import ROOT
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import numpy as np

class Bode:
    def __init__(self):
        self.figure = plt.figure()