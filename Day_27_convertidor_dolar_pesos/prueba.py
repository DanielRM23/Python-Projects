import tkinter as tk


#Se crea un objeto de la clase Tk
window = tk.Tk()

# Título 
window.title("GUI program")
# Tamaño de la ventana 
window.minsize(width=500, height=300)
#Label 
label = tk.Label(text="Holaaaaaaaaa", font=("Arial",24) )
#Esto es para que se centre 
#label.pack()
#Esto es para que esté a la izquierda
#label.pack(side="bottom")
#Esta es otra forma en la que se puede acomodar la cosa
label.grid(column=0,row=0)

#Botones 

#Esta función es para cuando se aprieta el boton 
def clicked_button():
#    label["text"] = "Has pulsado el botón correctamente"
    label["text"] = entry.get() 

#   'command' ejecuta la función llamada "clicked_button"
button = tk.Button(text="Click me", command=clicked_button)
new_button = tk.Button(text="New button")

button.grid(column=1,row=1)
new_button.grid(column=2, row=0)

#entrada 

#Esto es para que se abra un recuadro en donde se puede ingresar algún string
entry = tk.Entry(width=10)
#entry.pack()
entry.grid(column=3, row=2)

#Esto es para imprimir lo que escribí
print(entry.get())








#Esto siempre ponlo al final 
window.mainloop()


