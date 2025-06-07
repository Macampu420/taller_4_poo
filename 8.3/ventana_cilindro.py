import tkinter as tk
from cilindro import Cilindro

class VentanaCilindro:
    def __init__(self, contenedor):
        self.contenedor = contenedor
        self.contenedor.title("Cilindro")
        self.contenedor.geometry("300x180")
        self.contenedor.resizable(False, False)
        
        tk.Label(self.contenedor, text="Radio (cms):").place(x=20, y=20)
        self.radio_entry = tk.Entry(self.contenedor, width=15)
        self.radio_entry.place(x=120, y=20)
        
        tk.Label(self.contenedor, text="Altura (cms):").place(x=20, y=50)
        self.altura_entry = tk.Entry(self.contenedor, width=15)
        self.altura_entry.place(x=120, y=50)
        
        calcular_btn = tk.Button(self.contenedor, text="Calcular", command=self.calcular)
        calcular_btn.place(x=115, y=90)
        
        tk.Label(self.contenedor, text="Volumen (cm3):").place(x=20, y=130)
        self.volumen_label = tk.Label(self.contenedor, text="")
        self.volumen_label.place(x=130, y=130)
        
        tk.Label(self.contenedor, text="Superficie (cm2):").place(x=20, y=150)
        self.superficie_label = tk.Label(self.contenedor, text="")
        self.superficie_label.place(x=130, y=150)
    
    def calcular(self):
        try:
            radio = float(self.radio_entry.get())
            altura = float(self.altura_entry.get())
            cilindro = Cilindro(radio, altura)
            self.volumen_label.config(text=f"{cilindro.getVolumen():.2f}")
            self.superficie_label.config(text=f"{cilindro.getSuperficie():.2f}")
        except ValueError:
            self.volumen_label.config(text="Error")
            self.superficie_label.config(text="Error")