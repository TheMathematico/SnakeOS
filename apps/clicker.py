import customtkinter as ctk
import utility

# for functions, fg, bg are the main colors and when an s is added(e.g. fgs) 
# that means its a secondary color(e.g ForeGroundSecondary = fgs)

clicks = 0
clicks_add = 0
clicks_label0 = 0

income_delay = 50 #50 is 50 iterations, rougly 1 second
timer = 0

w=500
h=500

def update():
    global clicks
    global clicks_add
    global clicks_label0
    global timer, income_delay

    if timer == income_delay:
        clicks += clicks_add
        timer = 0
    else:
        timer+=1

    clicks_label0.configure(text=str(clicks))

def create_upgrade_section(image, title, cap, clicks, price, parent, image_size=(65, 65), w=500, h=120, fg="#14332A", fgs="#1A3C34", pad_x=5, pad_y=5):
    price_offset = 0    

    frame = ctk.CTkFrame(parent, w, h, fg_color=fg)
    frame.pack(padx=pad_x, pady=pad_y)
    frame.pack_propagate(False)

    top_frame = ctk.CTkFrame(frame, width=w, height=20, fg_color=fg)
    top_frame.pack(padx=0, pady=0, side="top")
    top_frame.pack_propagate(False)

    showcase = ctk.CTkScrollableFrame(frame, orientation="horizontal", width=w-35, height=120, fg_color=fg)
    showcase.pack(padx=5, pady=5, side="bottom")

    title_label = ctk.CTkLabel(top_frame, text=title, font=("monogram", 20), height=20)
    title_label.pack(padx=5, pady=0, side="left")

    def on_click():
        nonlocal showcase
        global clicks_add

        print("click")

        clicks_add += clicks
        print(clicks_add, " +++")

        to_image = utility.to_image("cursor.png", image_size)
        photo = ctk.CTkImage(to_image, to_image, image_size)

        puppet = ctk.CTkLabel(showcase, text="", image=photo, width=100, height=70)
        puppet.pack(padx=5, pady=0, side="left")

        puppet.image = photo

        print(puppet.master)
        print("Done")

    buy_btn = ctk.CTkButton(
        top_frame, 
        text=f"BUY({price + price_offset})", 
        font=("monogram", 20), 
        height=20, 
        fg_color="green", 
        hover_color=fgs,
        command=on_click
    )
    buy_btn.pack(padx=5, pady=0, side="left")

def open(cursor, bgs):
    if update not in utility.todo:
        global clicks_label0
        global w, h

        window = utility.create_window(w, h, "ZooClicker")
        window.function = update
        print(window)

        image = ctk.CTkImage(cursor, cursor, (50, 50))

        stats_frame = ctk.CTkFrame(window, width=w, height=70, fg_color=bgs)
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

        create_upgrade_section("cursor.png", "Cursors", 0, 2, 0, window)

        utility.todo.append(update)

