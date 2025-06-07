import math
from figura_geometrica import FiguraGeometrica

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.calcularVolumen()
        self.calcularSuperficie()
    
    def calcularVolumen(self):
        volumen = math.pi * (self.radio ** 2) * self.altura
        self.setVolumen(volumen)
        return volumen
    
    def calcularSuperficie(self):
        superficie = 2 * math.pi * self.radio * (self.radio + self.altura)
        self.setSuperficie(superficie)
        return superficie