import numpy as np

class Notas:
    def __init__(self, notas:list):
        self.notas = notas

    def promedio(self):
        resultado=np.average(self.notas)
        return resultado

    def desviacion(self):
        resultado=np.std(self.notas)
        return resultado

    def mayor(self):
        resultado=np.max(self.notas)
        return resultado

    def menor(self):
        resultado=np.min(self.notas)
        return resultado