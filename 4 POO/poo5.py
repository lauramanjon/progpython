import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1,text="Numero1")
        self.label1.grid(column=0,row=0)
        self.label2=tk.Label(self.ventana1,text="Numero 2:")
        self.label2.grid(column=0,row=1)
        self.dato1=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1,width=10,textvariable)

        self.boton1=tk.Button(self.ventana1,text="Suma",command=self.sumar)
        self.boton1.grid(column=0,row=2)
        self.label2=tk.Label(self.ventana1,text="resultado")
        self.label2.grid(column=0,row=3)
        self.ventana1.mainloop()

        

    def sumar(self):
        valor=int(self.dato.get())
        valor1=int(self.dato1.get())
        resultado=valor+valor1
        self.label2.configure(text=resultado)
        

    def ingresar(self):
        if self.dato1.get()=="juan" and self.dato2.get()=="abc123":
            self.ventana1.title("Correcto")
        else:
            self.ventana1.title("Incorrecto")

aplicacion1=Aplicacion() 
