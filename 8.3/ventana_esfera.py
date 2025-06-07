import tkinter as tk
from tkinter import ttk
from esfera import Esfera

class VentanaEsfera:
    def __init__(self, contenedor):
        self.contenedor = contenedor
        self.radio = tk.StringVar()
        self.volumen = tk.StringVar()
        self.superficie = tk.StringVar()
        self.campoRadio = None
        self.calcular = None
        
        self.init()
    
    def init(self):
        self.contenedor.title("Esfera")
        self.contenedor.geometry("300x180")
        
        tk.Label(self.contenedor, text="Radio (cms):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.campoRadio = tk.Entry(self.contenedor, textvariable=self.radio, width=20)
        self.campoRadio.grid(row=0, column=1, padx=5, pady=5)
        
        self.calcular = tk.Button(self.contenedor, text="Calcular", command=self.actionPerformed)
        self.calcular.grid(row=1, column=0, columnspan=2, pady=10)
        
        tk.Label(self.contenedor, text="Volumen (cm3):").grid(row=2, column=0, sticky="w", padx=5, pady=2)
        tk.Label(self.contenedor, textvariable=self.volumen).grid(row=2, column=1, sticky="w", padx=5, pady=2)
        
        tk.Label(self.contenedor, text="Superficie (cm2):").grid(row=3, column=0, sticky="w", padx=5, pady=2)
        tk.Label(self.contenedor, textvariable=self.superficie).grid(row=3, column=1, sticky="w", padx=5, pady=2)
    
    def actionPerformed(self):
        try:
            r = float(self.radio.get())
            esfera = Esfera(r)
            self.volumen.set(f"{esfera.getVolumen():.2f}")
            self.superficie.set(f"{esfera.getSuperficie():.2f}")
        except ValueError:
            self.volumen.set("Error")
            self.superficie.set("Error")