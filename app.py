from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
REPS = 0
COMPLETED = ""
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS, COMPLETED, TIMER
    window.after_cancel(TIMER)
    REPS = 0
    COMPLETED = ""
    completed_label.config(text=COMPLETED)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    # start_timer()


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    round_pomodoro = REPS % 8
    work_sec = WORK_MIN * 60
    short_brake_sec = SHORT_BREAK_MIN * 60
    long_brake_sec = LONG_BREAK_MIN * 60
    if round_pomodoro in (0, 2, 4, 6):
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif round_pomodoro in (1, 3, 5):
        count_down(short_brake_sec)
        timer_label.config(text="Break", fg=PINK)
    elif round_pomodoro == 7:
        count_down(long_brake_sec)
        timer_label.config(text="Break", fg=RED)
    REPS += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global REPS
    global COMPLETED
    global TIMER
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        if REPS % 2 == 1:
            COMPLETED += "✓"
            completed_label.config(text=COMPLETED)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40))
timer_label.grid(column=1, row=0)


button_start = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
button_start.grid(column=0, row=2)


button_reset = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
button_reset.grid(column=2, row=2)

completed_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
completed_label.grid(column=1, row=3)


window.mainloop()
