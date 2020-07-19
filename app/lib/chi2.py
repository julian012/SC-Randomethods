import numpy as np
from scipy.stats import chi2

class Chi2:

    def __init__(self, error, array, range=8):
        self.error = error
        self.array = array
        self.min_val = np.amin(array)
        self.max_val = np.amax(array)
        self.range = range
        self.expected_frequency = array.size/range

    def makeTest(self):
        interval = np.zeros(shape=(self.range,2))

        #Se obtienen los intervalos del la lista
        for i in range(self.range):
            if i == 0:
                initial = self.min_val
                final = initial + (self.max_val - self.min_val)/self.range
                interval[i] = [initial, final]
            else:
                initial = interval[i-1][1]
                final = initial + (self.max_val - self.min_val)/self.range
                interval[i] = [initial, final]

        #Sacar la frecuencia de un array
        hist, bin_edges = np.histogram(self.array, self.range)

        #Cambiar de vector a matriz
        hist_reshape = np.reshape(hist,(self.range,1))

        #Sumar matrices
        interval = np.hstack((interval, hist_reshape))
        
        #Obtener el chi cuadrado
        chi2_list = []
        for val in interval:
            c = pow(val[2] - self.expected_frequency, 2)/self.expected_frequency
            chi2_list = (np.append(chi2_list,c))

        #Sumar lista chi2
        self.sum_chi2 = np.sum(chi2_list)

        #Cambiar de vector a matriz de la lista chi2
        chi2_list_reshape = np.reshape(chi2_list,(self.range,1))

        #Sumar matrices 
        self.histogram = np.hstack((interval, chi2_list_reshape))

        #Se calcula el inverso de Chi2
        self.invChi2 = chi2.isf(self.error, self.range - 1)

        return np.where(self.invChi2 > self.sum_chi2, 'Pasaron la prueba de uniformidad', 'No pasaron la prueba de uniformidad')

    def getRange(self):
        return self.range
    
    def getExpectedFrequency(self):
        return self.expected_frequency
    
    def getMin(self):
        return self.min_val
    
    def getMax(self):
        return self.max_val
    
    def getHistogram(self):
        return self.histogram
    
    def getSumChi2(self):
        return self.sum_chi2
    
    def getInvChi2(self):
        return self.invChi2