#None of the variables here are customizable, if you want to customize them go to main.py

import customtkinter as ctk

BACKGROUND = ""
BACKGROUND_SECONDARY = ""
BACKGROUND_HOVER = ""

dragging = None
offset_x = 0
offset_y = 0

TOP_FRAME_HEIGHT = 0

apps_offset = 0

workspace = None
root = None

todo = []#list of functions the apps provide that the update loop in this file loops through and does

def start_drag(obj):
    global dragging
    global offset_x, offset_y
    global root

    x, y = root.winfo_pointerxy()

    if not dragging:
        dragging = obj

        offset_x = x - dragging.winfo_rootx()
        offset_y = y - dragging.winfo_rooty()
    else:
        dragging = None

def add_button(parent, height, width, text, fontsize, cmd, fg, hc, pad, side):
    a = ctk.CTkButton(
        parent, 
        height=height,
        width=width,
        font=("monogram", fontsize),
        text=text,
        command=cmd,
        fg_color=fg,
        corner_radius=15,
        hover_color=hc
    )

    a.pack(padx=0, pady=pad, side=side)

    return a

def create_window(width, height, title, fg):
    global workspace
    global TOP_FRAME_HEIGHT
    global todo

    if fg == 0:
        fg = BACKGROUND_HOVER

    window = ctk.CTkFrame(workspace, width=width, height=height, fg_color=fg)
    window.place(x=500, y=300)
    window.pack_propagate(False)

    top_frame = ctk.CTkFrame(window, width, TOP_FRAME_HEIGHT, 0, fg_color=BACKGROUND)
    top_frame.pack(padx=0, pady=0)
    top_frame.pack_propagate(False)
    top_frame.bind("<Button-1>", lambda event: start_drag(window))

    title_label = ctk.CTkLabel(top_frame, text=title, font=("monogram", 32))
    title_label.pack(padx=0, pady=0, side="left")
    title_label.bind("<Button-1>", lambda event: start_drag(window))

    def on_close():
        window.destroy()

        if window.function:
            print(window.function)
            todo.remove(window.function)
            print("removed.")

    close_btn = ctk.CTkButton(
        top_frame, 
        35, 
        TOP_FRAME_HEIGHT, 
        fg_color="red",
        font=("monogram", 32), 
        text="X", 
        corner_radius=0,
        command=on_close,
        hover_color="#d74665"
    )

    close_btn.pack(padx=0, pady=0, side="right")

    return window

def create_app(title, pfp, cmd):
    global workspace
    global apps_offset

    app = ctk.CTkFrame(workspace, width=100, height=120, fg_color="transparent", bg_color="transparent")
    app.place(x=5, y=5+apps_offset)

    image = ctk.CTkImage(pfp, pfp, (95, 90))

    p = ctk.CTkLabel(app, width=95, height=90, text="",  fg_color="transparent", image=image)
    p.pack(padx=5, pady=5)

    title_label = ctk.CTkLabel(app, text=title, font=("monogram", 24), text_color="white")
    title_label.pack(padx=0, pady=0)

    title_label.bind("<Button-1>", cmd)
    p.bind("<Button-1>", cmd)

    apps_offset += 130

def update_loop():
    global dragging
    global offset_x, offset_y 

    if dragging:
        x, y = root.winfo_pointerxy()

        parent = dragging.master

        parent_x = parent.winfo_rootx()
        parent_y = parent.winfo_rooty()

        dragging.place(x=x - offset_x - parent_x, y=y - offset_y - parent_y)

    for v in todo:
        v()

    root.after(20, update_loop)