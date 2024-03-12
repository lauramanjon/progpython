import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.scroll1 = tk.Scrollbar(self.ventana1, orient=tk.VERTICAL)
        self.listbox1=tk.Listbox(self.ventana1, selectmode=tk.MULTIPLE, yscrollcommand=self.scroll1.set)
        self.listbox1.grid(column=0,row=0)
        self.scroll1.configure(command=self.listbox1.yview)         
        self.scroll1.grid(column=1, row=0, sticky='NS')        
        self.listbox1.insert(0,"España")
        self.listbox1.insert(1,"Francia")
        self.listbox1.insert(2,"Alemania")
        self.listbox1.insert(3,"Inglaterra")
        self.listbox1.insert(4,"Holanda")
        self.listbox1.insert(5,"Italia")
        self.dato1=tk.StringVar()
        self.entry=tk.Entry(self.ventana1, width=20, textvariable=self.dato)
        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=2)
        self.label1=tk.Label(self.ventana1,text="Seleccionado:")
        self.label1.grid(column=0, row=3)
        self.ventana.mainloop()


    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            self.label1.configure(text=self.dato1.get()+''+self.listbox1.get(self.listbox1.curselection()[0]))
aplicacion1=Aplicacion()         
