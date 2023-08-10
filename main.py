import math
from tkinter import *
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
time = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(time)
    canvas.itemconfig(timer,  text='00:00')
    timer_label.config(text='Timer')
    checkmark_label.config(text=None)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        timer_label.config(text='Long Break', font=(FONT_NAME, 40, 'bold'), fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        timer_label.config(text='Short Break', font=(FONT_NAME, 40, 'bold'), fg=PINK, bg=YELLOW)
    else:
        count_down(WORK_MIN*60)
        timer_label.config(text='Work Time', font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = math.floor(count/60)
    sec = count % 60
    if sec < 10:
        sec = f'0{sec}'
    canvas.itemconfig(timer, text=f'{min}:{sec}')
    if count > 0:
        global time
        time = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ''
        for _ in range(math.floor(reps/2)):
            marks += '✓'
        checkmark_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(103, 112, image=tomato)
timer = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer_label = Label(text='Timer', font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

start = Button(text='Start', command=start_timer)
start.grid(column=0, row=2)

reset = Button(text='Reset', command=reset_timer)
reset.grid(column=2, row=2)


window.mainloop()