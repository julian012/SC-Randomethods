import numpy as np
from numpy import random
import math
from scipy.stats import norm

class MeanTest:

    def __init__(self, array, freedom):
        self.array = array
        self.freedom = freedom
        self.acceptance = 1 - freedom
        self.size = len(array)
        self.average = np.average(array)
        self.freedomRange = 1 - (self.freedom/2)
        self.z = norm.ppf(self.freedomRange)
        self.sub_l = (self.z*(1/math.sqrt(12*self.size)))
        self.li = 0.5 - self.sub_l
        self.ls = 0.5 + self.sub_l
        self.min = np.amin(self.array)
        self.max = np.amax(self.array)
        self.result = np.where(self.li <= self.average and self.average <= self.ls, 'Cumple', 'No cumple')

    def getArray(self):
        return self.array

    def getFreedom(self):
        return self.freedom

    def getAcceptance(self):
        return self.acceptance

    def getSize(self):
        return self.size

    def getAverage(self):
        return self.average

    def getFreedomRange(self):
        return self.freedomRange

    def getZ(self):
        return self.z

    def getLI(self):
        return self.li

    def getLS(self):
        return self.ls

    def getMin(self):
        return self.min

    def getMax(self):
        return self.max

    def getResult(self):
        return self.result

#array = random.rand(50)
#t = MeanTest(array,0.05)
#print(t.getMin())
#print(t.getMax())
#print(t.getAverage())
#print(t.getLI())
#print(t.getLS())
#print(t.getResult())