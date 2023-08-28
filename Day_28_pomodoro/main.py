import tkinter as tk 
import math 

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_time():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_mark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    
    reps+=1
    # Minutos que se trabajan en segundos
    work_sec = WORK_MIN * 60
    # Descanso corto en segundos
    short_break_sec = SHORT_BREAK_MIN*60
    # Descanso largo en segundos
    long_break_sec = LONG_BREAK_MIN*60

    if reps == 8:
        label.config(text = "Break" ,fg=RED)
        count_down(long_break_sec)

    elif reps%2 != 0:
        label.config(text = "Work" ,fg=PINK)
        count_down(work_sec)
    
    else:
        label.config(text = "Break" ,fg=GREEN)
        count_down(short_break_sec)
        


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer 
    count_min = math.floor(count / 60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}" )
    
    if count > 0:
        timer = window.after(1000, count_down, count-1)

    else:
        start_timer()

        mark =""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        
        check_mark.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #


# Se crea la ventana
window = tk.Tk()
window.title("Pomodoro")
window.config(padx= 100, pady=50, bg= YELLOW)


# Literalmente canvas es un lienzo sobre el cual se pondrán objetos (cosos de interés)
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Esto es para importar la imagen 
tomato_imagen = tk.PhotoImage(file="tomato.png")
# Con esto se pone la imagen sobre el canvas
# Es necesario especificar en donde se coloca la imagen y cual es 
canvas.create_image(100, 112, image= tomato_imagen)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# Se centra 
#canvas.pack()
canvas.grid(column=1, row=1)


#Se crean botones
boton_start = tk.Button(text="Start", command= start_timer)
boton_reset = tk.Button(text= "Reset", command= reset_time)

boton_start.grid(column=0, row=2)
boton_reset.grid(column=2, row=2)


#Se crean labels
label = tk.Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg= GREEN, bg=YELLOW)
check_mark = tk.Label(font=(FONT_NAME, 25, "bold"), fg=GREEN, bg= YELLOW )

label.grid(column=1, row=0)
check_mark.grid(column=1, row=3)




window.mainloop()