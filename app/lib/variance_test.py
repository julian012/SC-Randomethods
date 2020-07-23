import numpy as np
from numpy import random
import math
from scipy.stats import norm, chi2

class VarianceTest:

    def __init__(self, array, freedom):
        self.array = array
        self.freedom = freedom
        self.acceptance = 1 - freedom
        self.size = len(array)
        self.average = np.average(array)
        self.variace = np.var(array)
        self.half_freedom = self.freedom/2
        self.freedomRange = 1 - (self.freedom/2)
        self.invChi2 = chi2.isf(self.half_freedom, self.size - 1)
        self.invChi2_less_one = chi2.isf(1 - self.half_freedom, self.size - 1)
        self.li = self.invChi2/(12*(self.size - 1))
        self.ls = self.invChi2_less_one/(12*(self.size - 1))
        self.result = np.where(self.li >= self.variace and self.variace >= self.ls, 'Cumple', 'No cumple')

    def getArray(self):
        return self.array

    def getFreedom(self):
        return self.freedom

    def getAcceptance(self):
        return self.acceptance

    def getSize(self):
        return self.size

    def getVariance(self):
        return self.variace
    
    def getFreedomRange(self):
        return self.freedomRange
    
    def getLI(self):
        return self.li

    def getLS(self):
        return self.ls
    
    def getResult(self):
        return self.result

#array = random.rand(50)
#print(array)
#t = VarianceTest(array,0.05)

#print(t.getVariance())
#print(t.getLI())
#print(t.getLS())
#print(t.getResult())