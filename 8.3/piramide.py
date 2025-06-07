import math
from figura_geometrica import FiguraGeometrica

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.calcularVolumen()
        self.calcularSuperficie()
    
    def calcularVolumen(self):
        volumen = (self.base ** 2 * self.altura) / 3
        self.setVolumen(volumen)
        return volumen
    
    def calcularSuperficie(self):
        superficie = (self.base ** 2) + (2 * self.base * self.apotema)
        self.setSuperficie(superficie)
        return superficie