from tkinter import *
from tkinter import ttk
import tkinter as ttk

ventana = Tk()
ventana.title("Ejercicio_2")
# Crear frame principal
principal_Frame = ttk.Frame(ventana, width=200, height=200, bg="black")
principal_Frame.grid()

# Frame 1
gris_frame = ttk.Frame(principal_Frame, width=693, height=100, bg="gray40", relief="raised")
gris_frame.grid(column=0, row=0)

etqTexto = ttk.Label(gris_frame)
etqTexto.grid()

imagen = PhotoImage(file= 'Carrito.png')

etqImagen = ttk.Label(gris_frame, bg="gray40")
etqImagen.grid(column=0, row=0,sticky=(E))
etqImagen["image"]  = imagen

ttk.Label(gris_frame, text="Product management", bg="gray40", font=("Arial", 36, "bold"), foreground="white").grid(column=1, row=0, padx=10, pady=10)
ttk.Label(gris_frame, text="      ", bg="gray40", foreground="white").grid(column=2, row=0, padx=70, pady=10)

# Frame negro superior
negro_frame = ttk.Frame(principal_Frame, width=300, height=10, bg="black")
negro_frame.grid(column=0, row=1)

# Frame 2 
cafe_frame = ttk.Frame(principal_Frame, width=690, height=510, bg="#482525")
cafe_frame.grid(column=0, row=2)

#Frame 3
gran_frame = ttk.Frame(cafe_frame, width=690, height=260, bg="#482525")
gran_frame.grid(column=0, row=0)

#Frame 4
datos_frame = ttk.Frame(gran_frame, width=690, height=260, bg="#482525")
datos_frame.grid(column=0, row=0,pady=20)

ttk.Label(datos_frame, text="Id product:", bg="#482525", font=("Arial", 14, "bold"), foreground="white").grid(column=0, row=0, padx=10, pady=10, sticky=(W))
ttk.Label(datos_frame, text="_______________________", bg="#482525", font=("Arial", 14, "bold"), foreground="white").grid(column=1, row=0, padx=10)
Id_Product = ttk.Entry(datos_frame, width=15, font=("Arial", 14, "bold"), bg="#482525", foreground="white", justify=CENTER )
Id_Product.config(borderwidth=0, highlightthickness=0) # Configura los atributos para hacer el marco invisible
Id_Product.grid(column=1, row=0, padx=10, sticky=(N))

ttk.Label(datos_frame, text="Name:", bg="#482525", font=("Arial", 14, "bold"), foreground="white").grid(column=0, row=1, padx=10, pady=10, sticky=(W))
ttk.Label(datos_frame, text="_______________________", bg="#482525", font=("Arial", 14, "bold"), foreground="white").grid(column=1, row=1, padx=10)
NameE = ttk.Entry(datos_frame, width=15, font=("Arial", 14, "bold"), bg="#482525", foreground="white", justify=CENTER )
NameE.config(borderwidth=0, highlightthickness=0) # Configura los atributos para hacer el marco invisible
NameE.grid(column=1, row=1, padx=10, sticky=(N))

ttk.Label(datos_frame, text="Descripcion:", bg="#482525", font=("Arial", 14, "bold"), foreground="white").grid(column=0, row=2, padx=10, pady=10, sticky=(W))
ttk.Label(datos_frame, text="_______________________", bg="#482525", font=("Arial", 14, "bold"), foreground="white").grid(column=1, row=2, padx=10)
DescripcionE = ttk.Entry(datos_frame, width=15, font=("Arial", 14, "bold"), bg="#482525", foreground="white", justify=CENTER )
DescripcionE.config(borderwidth=0, highlightthickness=0) # Configura los atributos para hacer el marco invisible
DescripcionE.grid(column=1, row=2, padx=10, sticky=(N))

ttk.Label(datos_frame, text="quantity:", bg="#482525", font=("Arial", 14, "bold"), foreground="white").grid(column=0, row=3, padx=10, pady=10, sticky=(W))
ttk.Label(datos_frame, text="_______________________", bg="#482525", font=("Arial", 14, "bold"), foreground="white").grid(column=1, row=3, padx=10)
quantityE = ttk.Entry(datos_frame, width=15, font=("Arial", 14, "bold"), bg="#482525", foreground="white", justify=CENTER )
quantityE.config(borderwidth=0, highlightthickness=0) # Configura los atributos para hacer el marco invisible
quantityE.grid(column=1, row=3, padx=10, sticky=(N))

ttk.Label(datos_frame, text="Price:", bg="#482525", font=("Arial", 14, "bold"), foreground="white").grid(column=0, row=4, padx=10, pady=10, sticky=(W))
ttk.Label(datos_frame, text="_______________________", bg="#482525", font=("Arial", 14, "bold"), foreground="white").grid(column=1, row=4, padx=10)
PriceE = ttk.Entry(datos_frame, width=15, font=("Arial", 14, "bold"), bg="#482525", foreground="white", justify=CENTER )
PriceE.config(borderwidth=0, highlightthickness=0) # Configura los atributos para hacer el marco invisible
PriceE.grid(column=1, row=4, padx=10, sticky=(N))

#Frame 5
frame5 = ttk.Frame(gran_frame, width=690, height=260, bg="#482525")
frame5.grid(column=1, row=0,sticky=(N),pady=5,padx=30)

#Frame 6
botones_frame = ttk.Frame(frame5, width=690, height=70, bg="#482525")
botones_frame.grid(column=0, row=0,sticky=(N))


imagen2 = PhotoImage(file= 'lupa.png')
imagen2_reducida = imagen2.subsample(30, 30) # La imagen se reducirá a la mitad en ambas direcciones (horizontal y vertical)
etqImagen2 = ttk.Button(botones_frame,bg="#482525",activebackground="#482525")
etqImagen2.grid(column=0, row=0,padx=15, sticky=(E))
etqImagen2['image']=imagen2_reducida
etqImagen2.config(borderwidth=0, highlightthickness=0)

imagen3 = PhotoImage(file= 'Brocha.png')
imagen3_reducida = imagen3.subsample(13, 13) # La imagen se reducirá a la mitad en ambas direcciones (horizontal y vertical)
etqImagen3 = ttk.Button(botones_frame,bg="#482525",activebackground="#482525")
etqImagen3.grid(column=1, row=0,padx=5, sticky=(E))
etqImagen3['image']=imagen3_reducida
etqImagen3.config(borderwidth=0, highlightthickness=0)


BottonBack = ttk.Button(botones_frame,text="Back",  bg="#482525",activebackground="#482525", foreground="#7701da",activeforeground="#4c02a0",
font=("Arial", 14, "bold"))
BottonBack.grid(column=2,row=0,pady=15)
BottonBack.config(borderwidth=0, highlightthickness=0)

ttk.Label(botones_frame, text="                     ", bg="#482525", font=("Arial", 14, "bold"), foreground="white").grid(column=3, row=0)

#Frame 7

semaforo_frame = ttk.Frame(frame5, width=690, height=70, bg="#482525")
semaforo_frame.grid(column=0, row=1)


BottonSave = ttk.Button(semaforo_frame,text="Save",  width=15, bg="green",activebackground="#482525", foreground="white",activeforeground="#4c02a0",
font=("Arial", 14, "bold"))
BottonSave.grid(column=0,row=0, pady=10,sticky=(W))
BottonSave.config(borderwidth=0, highlightthickness=0)
ttk.Label(semaforo_frame, text="                     ", bg="#482525", font=("Arial", 14, "bold"), foreground="white").grid(column=1, row=0, padx=2)

BottonDelete = ttk.Button(semaforo_frame,text="Delete",  width=15, bg="Red",activebackground="#482525", foreground="white",activeforeground="#4c02a0",
font=("Arial", 14, "bold"))
BottonDelete.grid(column=0,row=1, pady=10, sticky=(W))
BottonDelete.config(borderwidth=0, highlightthickness=0)

BottonUpdate = ttk.Button(semaforo_frame,text="Update",  width=15, bg="Orange",activebackground="#482525", foreground="white",activeforeground="#4c02a0",
font=("Arial", 14, "bold"))
BottonUpdate.grid(column=0,row=2, pady=10, sticky=(W))
BottonUpdate.config(borderwidth=0, highlightthickness=0)

tabla_frame = ttk.Frame(gran_frame, width=690, height=70, bg="#482525")
tabla_frame.grid( row=1, columnspan=2)


# Crear encabezado de la tabla
ttk.Label(tabla_frame, text="idproduit", width=10, bg="gray", fg="white").grid(row=0, column=0)
ttk.Label(tabla_frame, text="namep", width=20, bg="gray", fg="white").grid(row=0, column=1)
ttk.Label(tabla_frame, text="description", width=30, bg="gray", fg="white").grid(row=0, column=2)
ttk.Label(tabla_frame, text="quantity", width=10, bg="gray", fg="white").grid(row=0, column=3)
ttk.Label(tabla_frame, text="unite_price", width=10, bg="gray", fg="white").grid(row=0, column=4)

# Crear datos de la tabla
data = [
    ("1", "Condia", "lait", "24", "100.0"),
    ("2", "la vache quirit", "fromage", "200", "300.0"),
    ("3", "hamound boualam", "boisson gaseuse", "98", "90.0"),
    ("4", "Mina", "Chocolat", "80", "50.0"),
    ("5", "Aroma", "cafe", "60", "80.0"),
    ("6", "Facto", "Facto", "7000", "600.0"),
    ("", "", "", "", ""),
    ("", "", "", "", ""),
    ("", "", "", "", "")
]

# Mostrar datos en la tabla
for i, row in enumerate(data):
    for j, item in enumerate(row):
        ttk.Label(tabla_frame, text=item, width=10 if j == 0 else 20 if j == 1 else 30 if j == 2 else 10 if j == 3 else 10, bg="white").grid(row=i+1, column=j, sticky=(W))

# Frame negro inferior
abajo_frame = ttk.Frame(principal_Frame, width=300, height=25, bg="black", relief="sunken")
abajo_frame.grid(column=0, row=3)

# Mostrar ventana
ventana.mainloop()