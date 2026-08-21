import customtkinter as ctk
import utility

clicks = 0
clicks_add = 0
clicks_label0 = 0

def update():
    global clicks
    global clicks_label0

    print("as")

    clicks_label0.configure(text=str(clicks))

def open(cursor, bgs):
    if update not in utility.todo:
        global clicks_label0

        window = utility.create_window(500, 500, "ZooClicker")
        window.function = update
        print(window)

        image = ctk.CTkImage(cursor, cursor, (50, 50))

        stats_frame = ctk.CTkFrame(window, width=500, height=70, fg_color=bgs)
        stats_frame.pack(padx=5, pady=5)
        stats_frame.pack_propagate(False)

        def on_click():
            global clicks
            nonlocal plus_label

            clicks+=1

        click_btn = ctk.CTkButton(stats_frame, text="", width=50, height=50, image=image, command=on_click)
        click_btn.pack(padx=5, pady=5, side="left")

        clicks_label = ctk.CTkLabel(stats_frame, text="Clicks: 0", font=("monogram", 32))
        clicks_label.pack(padx=5, pady=5, side="right")

        plus_label = ctk.CTkLabel(stats_frame, text="+1", font=("monogram", 32), text_color=bgs)
        plus_label.pack(padx=0, pady=5, side="right")

        clicks_label0 = clicks_label

        utility.todo.append(update)

