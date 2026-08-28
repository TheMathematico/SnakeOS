import customtkinter as ctk
import utility
import time

# for functions, fg, bg are the main colors and when an s is added(e.g. fgs) 
# that means its a secondary color(e.g ForeGroundSecondary = fgs)

clicks = 0
clicks_add = 0
clicks_label0 = 0
income_delay = 50 #50 is 50 iterations, 50 iterations = rougly 1 second
timer = 0

w=500
h=500

sections = {}

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

def create_upgrade_section(image, title, cap, clicksgive, price, parent, image_size=(65, 65), w=500, h=120, fg="#14332A", fgs="#14332A", pad_x=5, pad_y=5):
    global sections

    if not title in sections:
        sections[title] = 0

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

    amount_label = ctk.CTkLabel(top_frame, text=f"0/{cap}", font=("monogram", 20), height=20)
    amount_label.pack(padx=5, pady=0, side="left")

    def createPuppet():
        nonlocal amount_label
        nonlocal price_offset

        to_image = utility.to_image(image, image_size)
        photo = ctk.CTkImage(to_image, to_image, image_size)

        puppet = ctk.CTkLabel(showcase, text="", image=photo, width=100, height=70)
        puppet.pack(padx=5, pady=0, side="left")

        puppet.image = photo

        amount_label.configure(text=f"{sections[title]}/{cap}")

    for i in range(sections[title]):
        createPuppet()

    def on_click():
        nonlocal buy_btn
        nonlocal price_offset
        global clicks
        global clicks_add

        if clicks >= price + price_offset and sections[title] <= cap:
            sections[title] += 1
            createPuppet()

            price_offset += (price + price_offset) / 10
            clicks -= price
            clicks_add += clicksgive
        else:
            buy_btn.configure(fg_color="red", hover_color="red")
            frame.after(200, lambda: buy_btn.configure(fg_color="green", hover_color=fgs))
            

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

        upgrades_frame = ctk.CTkScrollableFrame(window, width=w, height=410, fg_color=bgs)
        upgrades_frame.pack(padx=5, pady=5)

        def on_click():
            global clicks
            nonlocal plus_label

            clicks+=1

        click_btn = ctk.CTkButton(stats_frame, text="", width=50, height=50, image=image, command=on_click)
        click_btn.pack(padx=5, pady=5, side="left")

        click_btn.image = image

        clicks_label = ctk.CTkLabel(stats_frame, text="Clicks: 0", font=("monogram", 32))
        clicks_label.pack(padx=5, pady=5, side="right")

        plus_label = ctk.CTkLabel(stats_frame, text="+1", font=("monogram", 32), text_color=bgs)
        plus_label.pack(padx=0, pady=5, side="right")

        clicks_label0 = clicks_label

        start = time.perf_counter()

        create_upgrade_section("cursor.png", "Cursors", cap=20, clicksgive=1, price=30, parent=upgrades_frame)
        create_upgrade_section("ant.png", "ants", cap=20, clicksgive=2, price=50, parent=upgrades_frame)
        create_upgrade_section("snail.png", "snails", cap=20, clicksgive=3, price=150, parent=upgrades_frame)
        create_upgrade_section("gecko.png", "geckos", cap=20, clicksgive=5, price=300, parent=upgrades_frame)
        create_upgrade_section("frog.png", "frogs", cap=20, clicksgive=7, price=500, parent=upgrades_frame)
        create_upgrade_section("fish.png", "fish", cap=20, clicksgive=9, price=1000, parent=upgrades_frame)
        create_upgrade_section("pigeon.png", "pigeons", cap=20, clicksgive=12, price=3000, parent=upgrades_frame)

        print("UPGRADES:", time.perf_counter() - start)

        utility.todo.append(update)

