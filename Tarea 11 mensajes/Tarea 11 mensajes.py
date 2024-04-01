import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.labelframe1=ttk.LabelFrame(self.ventana1, text="Cálculo de raiz cuadrada")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10)
        self.agregar_componentes()
        self.agregar_menu()
        self.ventana1.mainloop()

    def agregar_componentes(self):
        self.label1=ttk.Label(self.labelframe1, text="Ingrese valor de a:")
        self.label1.grid(column=0, row=0, padx=5, pady=5, sticky="e")
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe1, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.labelframe1, text="Ingrese el valor de b:")
        self.label2.grid(column=0, row=1, padx=5, pady=5, sticky="e")
        self.dato2=tk.StringVar()
        self.entry2=ttk.Entry(self.labelframe1, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1, padx=5, pady=5)
        self.label3=ttk.Label(self.labelframe1, text="Ingrese el valor de c:")
        self.label3.grid(column=0, row=2, padx=5, pady=5, sticky="e")
        self.dato3=tk.StringVar()
        self.entry3=ttk.Entry(self.labelframe1, textvariable=self.dato3)
        self.entry3.grid(column=1, row=2, padx=5, pady=5)
        
        self.boton1=ttk.Button(self.labelframe1, text="Calcular", command=self.calcular)
        self.boton1.grid(column=1, row=3, padx=5, pady=5, sticky="we")

    def agregar_menu(self):
        self.menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=self.menubar1)
        self.opciones1 = tk.Menu(self.menubar1, tearoff=0)
        self.opciones1.add_command(label="Salir", command=self.salir)
        self.menubar1.add_cascade(label="Opciones", menu=self.opciones1)    

    def calcular(self):
        if self.dato1.get()=="" or self.dato2.get()=="" or self.dato3.get()=="":
            mb.showerror("Cuidado","No puede dejar los cuadros de entrada de números vacíos")
        else:
            a=int(self.dato1.get())
            b=int(self.dato2.get())
            c=int(self.dato3.get())
            contenidoRaiz=b*b-4*a*c
            if contenidoRaiz<0:
                mb.showerror("Solucion","Soluciones complejas")
            else:
                raiz=sqrt(contenidoRaiz)
                x1=(-b+raiz)/2*a
                x2=(-b-raiz)/2*a
                solucion="x1="+x1+"x2="+x2
                mb.showinfo("Solucion",solucion)

    def salir(self):
        respuesta=mb.askyesno("Cuidado","¿Quere salir del programa?")
        if respuesta==True:
            sys.exit()

aplicacion1=Aplicacion() 
