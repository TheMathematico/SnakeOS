import customtkinter as ctk
import time
import utility

time_label0 = 0

def update_time():
    global time_label0

    time_label0.configure(text=time.strftime("%H:%M:%S"))

def open():
    global time_label0

    if update_time not in utility.todo:

        window = utility.create_window(200, 100, "time", 0)
        window.function = update_time
        print(window)

        time_label = ctk.CTkLabel(window, text="00:00:00 PM/AM", font=("monogran", 16))
        time_label.pack(padx=0, pady=0, anchor="center")

        time_label0 = time_label

        utility.todo.append(update_time)

        update_time()