import math
from figura_geometrica import FiguraGeometrica

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.calcularVolumen()
        self.calcularSuperficie()
    
    def calcularVolumen(self):
        volumen = (4/3) * math.pi * (self.radio ** 3)
        self.setVolumen(volumen)
        return volumen
    
    def calcularSuperficie(self):
        superficie = 4 * math.pi * (self.radio ** 2)
        self.setSuperficie(superficie)
        return superficie