import math

class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0
    
    def setVolumen(self, volumen):
        self.volumen = volumen
    
    def setSuperficie(self, superficie):
        self.superficie = superficie
    
    def getVolumen(self):
        return self.volumen
    
    def getSuperficie(self):
        return self.superficie