import tkinter as tk
from notas import Notas

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de notas")
        self.geometry("280x325")
        self.elementos()

    def popup(self):
        ventana2=tk.Toplevel(self)
        ventana2.title("Error")
        tk.Label(ventana2, text="Entrada inválida. Por favor ingrese valores numéricos.",wraplength=150).pack(padx=30, pady=20)
        tk.Button(ventana2, text="Cerrar", command=ventana2.destroy).pack(pady=(0,10))

    def calcular(self):
        try:
            lista=[]
            lista.append(float(self.entry1.get()))
            lista.append(float(self.entry2.get()))
            lista.append(float(self.entry3.get()))
            lista.append(float(self.entry4.get()))
            lista.append(float(self.entry5.get()))
            notas1=Notas(lista)
            self.avg_label.config(text=f"Promedio: {notas1.promedio()}")
            self.dv_label.config(text=f"Desviación estandar: {notas1.desviacion()}")
            self.max_label.config(text=f"Nota máxima: {notas1.mayor()}")
            self.min_label.config(text=f"Nota mínima: {notas1.menor()}")
        except:
            self.popup()

    def limpiar(self):
        self.avg_label.config(text=f"")
        self.dv_label.config(text=f"")
        self.max_label.config(text=f"")
        self.min_label.config(text=f"")     
    
    def elementos(self):
        tk.Label(self,text="Ingrese las notas a continuación").grid(row=0,column=0,columnspan=5,padx=5,pady=(20,10))

        tk.Label(self,text="Nota 1:").grid(row=1,column=0,padx=30,pady=1)
        tk.Label(self,text="Nota 2:").grid(row=2,column=0,padx=30,pady=1)
        tk.Label(self,text="Nota 3:").grid(row=3,column=0,padx=30,pady=1)
        tk.Label(self,text="Nota 4:").grid(row=4,column=0,padx=30,pady=1)
        tk.Label(self,text="Nota 5:").grid(row=5,column=0,padx=30,pady=1)

        self.entry1=tk.Entry(self)
        self.entry2=tk.Entry(self)
        self.entry3=tk.Entry(self)
        self.entry4=tk.Entry(self)
        self.entry5=tk.Entry(self)

        self.entry1.grid(row=1,column=1,padx=(0,30))
        self.entry2.grid(row=2,column=1,padx=(0,30))
        self.entry3.grid(row=3,column=1,padx=(0,30))
        self.entry4.grid(row=4,column=1,padx=(0,30))
        self.entry5.grid(row=5,column=1,padx=(0,30))

        tk.Button(self, text="Calcular",command=self.calcular).grid(row=7, column=0,columnspan=2,pady=10)
        tk.Button(self, text="Limpiar",command=self.limpiar).grid(row=7, column=1,columnspan=2)

        self.avg_label = tk.Label(self,text="")
        self.dv_label = tk.Label(self,text="")
        self.max_label = tk.Label(self,text="")
        self.min_label = tk.Label(self,text="")

        self.avg_label.grid(row=9, column=0,columnspan=2)
        self.dv_label.grid(row=11, column=0,columnspan=2)
        self.max_label.grid(row=13, column=0,columnspan=2)
        self.min_label.grid(row=15, column=0,columnspan=2)