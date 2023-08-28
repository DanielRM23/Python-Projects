import tkinter as tk
from tkinter import messagebox
import random
import pyperclip 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    #Se copia la conraseña en la enrtrada 
    entrada3.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website_introducido = entrada1.get()
    email_introducido = entrada2.get()
    contraseña_introducida = entrada3.get()
    
    #messagebox.showinfo(title="Title", message="Message")

    # Se crea el archivo con el cual se trabaja y se guardan los datos que se introducen 
    if len(website_introducido)==0 or len(contraseña_introducida)==0 :
        messagebox.showwarning(title="Error", message="No dejes nada en blanco, por fa")
    
    else:
        is_ok = messagebox.askokcancel(title=website_introducido, message=f"Estos son los valores introducidos\nEmail: \n{email_introducido}\nContraseña: \n{contraseña_introducida} \n¿Es correcto?")
        if is_ok:
            with open("contraseñas.txt", "a") as data_file:
                data_file.write(f"{website_introducido} | {email_introducido} | {contraseña_introducida} \n")
                entrada1.delete(0, tk.END)
                #entrada2.delete(0,END
                entrada3.delete(0, tk.END)
# ---------------------------- UI SETUP ------------------------------- #



# Se crea la ventana
window = tk.Tk()
window.title("Gestor de contraseñas")
#window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

# Se crea el canvas 
canvas = tk.Canvas(width=200, height=200)
# Se "importa" la imagen
imagen = tk.PhotoImage(file="logo.png")
# Se crea la imagen 
canvas.create_image(100, 100, image=imagen)
canvas.grid(column=1, row=0)


#Se crean los labels 
label1 = tk.Label(text="Website: ")
label2 = tk.Label(text="Email/Username: ")
label3 = tk.Label(text= "Password: ")

label1.grid(column=0, row=1)
label2.grid(column=0, row=2)
label3.grid(column=0, row=3)

# Se crean las entradas de la información 
entrada1 = tk.Entry(width=40)
entrada1.focus()
entrada2 = tk.Entry(width=40)
entrada2.insert(0, "DanielRM@ciencias.unam.mx")
entrada3 = tk.Entry(width=21)

entrada1.grid(column=1, row=1, columnspan=2)
entrada2.grid(column=1, row=2, columnspan=2)
entrada3.grid(column=1, row=3)

# Se crean los botones 
boton1 = tk.Button(text="Generate psswrd", command=generate_password)
boton2 = tk.Button(text= "Add", width=35, command=save)


boton1.grid(column=2, row=3)
boton2.grid(column=1, row=4, columnspan=2)

















window.mainloop()