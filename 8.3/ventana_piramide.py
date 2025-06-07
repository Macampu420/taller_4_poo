import tkinter as tk
from tkinter import ttk
from piramide import Piramide

class VentanaPiramide:
    def __init__(self, contenedor):
        self.contenedor = contenedor
        self.base = tk.StringVar()
        self.altura = tk.StringVar()
        self.apotema = tk.StringVar()
        self.volumen = tk.StringVar()
        self.superficie = tk.StringVar()
        self.campoBase = None
        self.campoAltura = None
        self.campoApotema = None
        self.calcular = None
        
        self.init()
    
    def init(self):
        self.contenedor.title("Pirámide")
        self.contenedor.geometry("300x250")
        self.contenedor.resizable(False, False)
        
        frame_principal = tk.Frame(self.contenedor)
        frame_principal.pack(padx=10, pady=10, fill="both", expand=True)
        
        tk.Label(frame_principal, text="Base (cms):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.campoBase = tk.Entry(frame_principal, textvariable=self.base, width=15)
        self.campoBase.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_principal, text="Altura (cms):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.campoAltura = tk.Entry(frame_principal, textvariable=self.altura, width=15)
        self.campoAltura.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(frame_principal, text="Apotema (cms):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.campoApotema = tk.Entry(frame_principal, textvariable=self.apotema, width=15)
        self.campoApotema.grid(row=2, column=1, padx=5, pady=5)
        
        self.calcular = tk.Button(frame_principal, text="Calcular", command=self.actionPerformed)
        self.calcular.grid(row=3, column=0, columnspan=2, pady=10)
        
        tk.Label(frame_principal, text="Volumen (cm3):").grid(row=4, column=0, sticky="w", padx=5, pady=2)
        tk.Label(frame_principal, textvariable=self.volumen).grid(row=4, column=1, sticky="w", padx=5, pady=2)
        
        tk.Label(frame_principal, text="Superficie (cm2):").grid(row=5, column=0, sticky="w", padx=5, pady=2)
        tk.Label(frame_principal, textvariable=self.superficie).grid(row=5, column=1, sticky="w", padx=5, pady=2)
    
    def actionPerformed(self):
        try:
            b = float(self.base.get())
            h = float(self.altura.get())
            a = float(self.apotema.get())
            piramide = Piramide(b, h, a)
            self.volumen.set(f"{piramide.getVolumen():.2f}")
            self.superficie.set(f"{piramide.getSuperficie():.2f}")
        except ValueError:
            self.volumen.set("Error")
            self.superficie.set("Error")