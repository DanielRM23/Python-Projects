import tkinter as tk

def resume_execution():
    print("¡Pausa terminada!")

def pause_execution():
    print("Pausa iniciada...")
    root.after(2000, resume_execution)  # Pausa de 2000 milisegundos (2 segundos)

root = tk.Tk()
root.title("Pausa con Tkinter")

start_button = tk.Button(root, text="Iniciar Pausa", command=pause_execution)
start_button.pack(pady=10)

root.mainloop()
