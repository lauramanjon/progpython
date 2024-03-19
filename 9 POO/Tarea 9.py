import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        
        opciones1 = tk.Menu(menubar1)
        
        opciones1.add_command(label="Dimensionar", command=self.fijartamano)
        
        opciones1.add_separator()
        
        opciones1.add_command(label="Salir", command=self.finalizar)
        
        menubar1.add_cascade(label="Opciones", menu=opciones1)

        self.label1=ttk.Label(text="Ancho:")
        self.laberl1.grif(column=0, row=0)

        self.ancho=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana1, width=10, textvariable=self.ancho)
        self.entry1.grid(column=1, row=0)

        self.label2=ttk.Label(text="Alto:")
        self.label2.grid(column=0, row=1)

        self.alto=tk.StringVar()
        self.entry2=ttk.Entry(self.ventana1, width=10, textvariable=self.alto)
        self.entry2.grid(column=1, row=1)

        self.ventana1.mainloop()

    def fijartamano(self):
        self.ventana1.geometry(self.ancho.get()+"x"+self.alto.get())

    def finalizar(self):
        sys.exit()



        
        
