import tkinter as tk

def agregar_alumno():
    codigo=codigo_entry.get()
    nombrealumno=nombrealumno_entry.get()
    apellidosalumno=apellidosalumno_entry.get()
    nota=nota_entry.get()

    with open("alumnos.txt", "a") as archivo:
        archivo.write(datos_alumno)
        
codigo_entry.delete(0, 'end')
nombrealumno_entry.delete(0, 'end')
apellidosalumno_entry.delete(0, 'end')
nota_entry.delete(0, 'end')

ventana = tk.Tk()
ventana.title("Notas de los alumnos")

tk.Label(ventana, text="Código:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(ventana, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
tk.Label(ventana, text="Apellidos:").grid(row=2, column=0, padx=5, pady=5)
tk.Label(ventana, text="Nota:").grid(row=3, column=0, padx=5, pady=5)

codigo_entry = tk.Entry(ventana)
codigo_entry.grid(row=0, column=1, padx=5, pady=5)

nombre_entry = tk.Entry(ventana)
nombre_entry.grid(row=1, column=1, padx=5, pady=5)

apellidos_entry = tk.Entry(ventana)
apellidos_entry.grid(row=2, column=1, padx=5, pady=5)

nota_entry = tk.Entry(ventana)
nota_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Button(ventana, text="Añadir un alumno", command=agregar_alumno).grid(row=4, column=0, columnspan=2, padx=5, pady=5)

ventana.mainloop()
