import numpy as np
from numpy import random
import math
from scipy.stats import kstwo

class KS:

    def __init__(self, array, freedom, range=8):
        self.array = array
        self.freedom = freedom
        self.acceptance = 1 - freedom
        self.size = len(array)
        self.average = np.average(array)
        self.min_val = np.amin(self.array)
        self.max_val = np.amax(self.array)
        self.range = range
    
    def makeTest(self):
        interval = np.zeros(shape=(self.range,2))

        for i in range(self.range):
            if i == 0:
                initial = self.min_val
                final = initial + (self.max_val - self.min_val)/self.range
                interval[i] = [initial, final]
            else:
                initial = interval[i-1][1]
                final = initial + (self.max_val - self.min_val)/self.range
                interval[i] = [initial, final]
        
        self.interval = interval
        
        #Sacar la frecuencia de un array
        hist, bin_edges = np.histogram(self.array, self.range)
        self.hist = hist

        #Cambiar de vector a matriz
        hist_reshape = np.reshape(hist,(self.range,1))
        sum_hist_reshape = np.sum(hist_reshape)

        #Sumar matrices
        interval = np.hstack((interval, hist_reshape))

        #En caso de necesitar hacer un ajuste
        if sum_hist_reshape == self.size:
            interval = np.hstack((interval, hist_reshape))
        else:
            diference = self.size - sum_hist_reshape
            hist_reshape[len(hist_reshape) - 1] = hist_reshape[len(hist_reshape) - 1] + diference

        self.numericalCorrelation = hist_reshape
        
        #Se agrega la columna de frecuencia acumulada
        accumulate = np.cumsum(hist_reshape)
        self.accumulate = accumulate
        accumulate_reshape = np.reshape(accumulate,(self.range,1))
        
        #Se agrega la frecuencia acumulada a la matriz
        interval = np.hstack((interval, accumulate_reshape))
        
        #Se genera la probabilidad obtenida acumulada
        accumulateProbability = self.setAccumulateProbability(accumulate)
        self.accumulateProbability = accumulateProbability
        accumulateProbability_reshape = np.reshape(accumulateProbability, (self.range, 1))

        #Se agrega la frecuencia acumulada a la matriz
        interval = np.hstack((interval, accumulateProbability_reshape))

        #Se genera la frecuencia esperada
        cumulativeExpectedFrecuency = self.setCumulativeExpectedFrecuency()
        self.cumulativeExpectedFrecuency = cumulativeExpectedFrecuency
        cumulativeExpectedFrecuency_reshape = np.reshape(cumulativeExpectedFrecuency, (self.range, 1))

        #Se agrega la frecuencia acumulada a la matriz
        interval = np.hstack((interval, cumulativeExpectedFrecuency_reshape))

        #Se calcula la probabilidad esperada
        expectedProbability = self.setExpectedProbability(cumulativeExpectedFrecuency)
        self.expectedProbability = expectedProbability
        expectedProbability_reshape = np.reshape(expectedProbability, (self.range, 1))

        #Se agrega la frecuencia acumulada a la matriz
        interval = np.hstack((interval, expectedProbability_reshape))

        #Se calcula la diferencia
        self.diference = self.setDiference(accumulateProbability,expectedProbability)

        self.max_diference = np.amax(self.diference)
        self.ks_inv = kstwo.isf(self.freedom,self.size)
        self.result = np.where(self.max_diference < self.ks_inv, 'Cumple', 'No cumple')
        self.total = interval
    
    def setAccumulateProbability(self, accumulate):
        a = []
        for val in accumulate:
            a.append(val/self.size)
        return a
    
    def setCumulativeExpectedFrecuency(self):
        a = []
        b = 0
        for i in range(self.range):
            if len(a) == 0:
                b = self.size/self.range
            else:
                b = b + (self.size/self.range)
            a.append(b)
        return a
    
    def setExpectedProbability(self, cumulativeExpectedFrecuency):
        a = []
        for i in cumulativeExpectedFrecuency:
            a.append(i/self.size)
        return a
    
    def setDiference(self,cumulativeExpectedFrecuency,expectedProbability):
        a = []
        for i in range(self.range):
            a.append(abs(cumulativeExpectedFrecuency[i] - expectedProbability[i]))
        return a
    
    # Retorna los intervalos
    def getInterval(self):
        return self.interval

    # Retorna las frecuencias obtenidas
    def getHist(self):
        return self.hist
    
    # Retorna la correlacion numerica
    def getNumericalCorrelation(self):
        return self.numericalCorrelation
    
    # Retorna la frecuencia acumulada
    def getAccumulate(self):
        return self.accumulate
    
    # Retorna la probabilidad obtenida acumulada
    def getAccumulateProbability(self):
        return self.accumulateProbability
    
    # Retorna la frecuencia esperada
    def getCumulativeExpectedFrecuency(self):
        return self.cumulativeExpectedFrecuency
    
    # Retoran la probabilidad esperada
    def getExpectedProbability(self):
        return self.expectedProbability
    
    # Retoran la diferencia
    def getDiference(self):
        return self.diference
    
    # Retorna la diferencia maxima
    def getMaxDiference(self):
        return self.max_diference
    
    # Retorna el inverso de KS
    def getKsInv(self):
        return self.ks_inv
    
    # Retorna el resultado
    def getResult(self):
        return self.result
    
    # Retoran la matriz con la tabla
    def getTotal(self):
        return self.total

#array = random.rand(50)
#t = KS(array,0.05, range=10)
#t.makeTest()
