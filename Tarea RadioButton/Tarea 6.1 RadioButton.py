import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.seleccion.set(2)
        self.radio1=tk.Radiobutton(self.ventana1,text="Sumar", variable=self.seleccion, value=1)
        self.radio1.grid(column=1, row=2)
        self.radio2=tk.Radiobutton(self.ventana1,text="Restar", variable=self.seleccion, value=2)
        self.radio2.grid(column=1, row=3)
        self.boton1=tk.Button(self.ventana1, text="Multiplicar", command=self.mostrarseleccionado)
        self.boton1.grid(column=1, row=4)
        self.label1=tk.Label(self.ventana1,text="Dividir")
        self.label1.grid(column=0, row=3)
        self.boton1=tk.Button(self.ventana1, text="Multiplicar", command=self.mostrarseleccionado)
        self.boton1.grid(column=1, row=4)
        self.label1=tk.Label(self.ventana1,text="Dividir")
        self.label1.grid(column=0, row=6)

        
        self.ventana1.mainloop()

    def mostrarseleccionado(self):
        if self.seleccion.get()==1:
            suma=int(self.dato1.get())+int(self.dato2.get())
            self.label3.configure(text=suma)
        if self.seleccion.get()==2:
            resta=int(self.dato1.get())-int(self.dato2.get())
            self.label3.configure(text=resta)
        if self.seleccion.get()==3:
            multi=int(self.dato1.get())*int(self.dato2.get())
            self.label3.configure(text=multi)
        if self.seleccion.get()==4:
            division=int(self.dato1.get())//int(self.dato2.get())
            self.label4.configure(text=division)
        

aplicacion=Aplicacion()
        
