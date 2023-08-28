import tkinter as tk 


# Se define primero la ventana 
window = tk.Tk()


# Título 
window.title("Convertidor Dolar a Pesos (MXN) julio 2023")
# Tamaño de la ventana 
window.minsize(width=200, height=200)
window.config(padx=20, pady=40)

# Se definen los labels
label1= tk.Label(text=" dólar(es)", font=("Arial",16) )
label2= tk.Label(text=" equivale(n) a ", font=("Arial",16) )
label3= tk.Label(text=" pesos (MXN) ", font=("Arial",16))
label4 = tk.Label(text=" ")


label1.grid(column=2, row=0)
label2.grid(column=0, row=1)
label3.grid(column=2, row=1)
label4.grid(column=1, row=1)


#Botones 

def presionar():
    """Función que cambia horas a minutos"""
    valor_dolar_introducido = int(entrada.get())
    valor_pesos = valor_dolar_introducido * 16.82
    label4["text"] = valor_pesos

# Se definen los botones 
boton = tk.Button(text=" Calcular ", command=presionar)
boton.grid(column=1, row=3)


# Se define la entrada del texto 
entrada = tk.Entry(width=10)
entrada.grid(column=1, row=0)




#Esto siempre se pone 
window.mainloop()