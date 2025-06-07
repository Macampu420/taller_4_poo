import tkinter as tk
from ventana_cilindro import VentanaCilindro
from ventana_esfera import VentanaEsfera
from ventana_piramide import VentanaPiramide

class VentanaPrincipal:
    def __init__(self, contenedor):
        self.contenedor = contenedor
        self.cilindro = None
        self.esfera = None
        self.piramide = None
        
        self.init()
    
    def init(self):
        self.contenedor.title("Figuras")
        self.contenedor.geometry("300x100")
        
        frame = tk.Frame(self.contenedor)
        frame.pack(pady=20)
        
        self.cilindro = tk.Button(frame, text="Cilindro", command=self.abrir_cilindro)
        self.cilindro.pack(side=tk.LEFT, padx=5)
        
        self.esfera = tk.Button(frame, text="Esfera", command=self.abrir_esfera)
        self.esfera.pack(side=tk.LEFT, padx=5)
        
        self.piramide = tk.Button(frame, text="Pirámide", command=self.abrir_piramide)
        self.piramide.pack(side=tk.LEFT, padx=5)
    
    def actionPerformed(self):
        pass
    
    def abrir_cilindro(self):
        ventana = tk.Tk()
        app = VentanaCilindro(ventana)
    
    def abrir_esfera(self):
        ventana = tk.Toplevel()
        ventana.transient(self.contenedor)
        ventana.grab_set()
        app = VentanaEsfera(ventana)
    
    def abrir_piramide(self):
        ventana = tk.Toplevel()
        ventana.transient(self.contenedor)
        ventana.grab_set()
        app = VentanaPiramide(ventana)