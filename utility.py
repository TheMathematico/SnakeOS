#None of the variables here are customizable, if you want to customize them go to main.py

import customtkinter as ctk
import time
from PIL import Image

BACKGROUND = "#0B1F1A"
BACKGROUND_SECONDARY = "#14332A"
BACKGROUND_HOVER = "#1A3C34"

#this is used for making the time label on the taskbar change colors(aka be rainbow)
colors = [
    "#134D1D",
    "#175A21",
    "#1B6725",
    "#20752A",
    "#27842F",
    "#2E9335",
    "#36A33C",
    "#3DB343",
    "#45C34A",
    "#4DCE50",
    "#55D756",
    "#5DE05C",
    "#65E762",
    "#6DED68",
    "#75F16E",
    "#7DF474",
    "#85F77A",
    "#7DF474",
    "#75F16E",
    "#6DED68",
    "#65E762",
    "#5DE05C",
    "#55D756",
    "#4DCE50",
    "#45C34A",
    "#3DB343",
    "#36A33C",
    "#2EA335",
    "#27842F",
    "#20752A",
    "#1B6725",
    "#175A21",
    "#134D1D",
]
counter = 0
index = 0

dragging = None
offset_x = 0
offset_y = 0

TOP_FRAME_HEIGHT = 0

apps_offsetx = 0
apps_offsety = 0

workspace = None
root = None
time_label = None

stupid_clicker_app = False #because it's insanely glitchy dragging any window over the window of the
                       #clicker app, the clicker app will be lifted everytime a window is created

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

def add_button(parent, height, width, text, fontsize = 32, cmd = None, fg=BACKGROUND_SECONDARY, hc=BACKGROUND_HOVER, tc="white", pad=0, side="bottom"):
    def on_click():
        cmd()

    a = ctk.CTkButton(
        parent,
        height=height,
        width=width,
        font=("Noto Sans Symbols 2", fontsize),
        text=text,
        command=on_click,
        fg_color=fg,
        corner_radius=15,
        hover_color=hc,
        text_color=tc
    )

    a.pack(padx=0, pady=pad, side=side)

    return a

def create_window(width, height, title, fg = BACKGROUND_HOVER, top_frame_fg = BACKGROUND):
    global workspace, stupid_clicker_app
    global TOP_FRAME_HEIGHT
    global todo

    window = ctk.CTkFrame(workspace, width=width, height=height, fg_color=fg, corner_radius=0)
    window.place(x=500, y=300)
    window.pack_propagate(False)

    if title == "ZooClicker":
        stupid_clicker_app = window

    if stupid_clicker_app:
        stupid_clicker_app.lift()

    top_frame = ctk.CTkFrame(window, width, TOP_FRAME_HEIGHT, 0, fg_color=top_frame_fg)
    top_frame.pack(padx=0, pady=0)
    top_frame.pack_propagate(False)
    top_frame.bind("<Button-1>", lambda event: start_drag(window))

    title_label = ctk.CTkLabel(top_frame, text=title, font=("monogram", 32))
    title_label.pack(padx=0, pady=0, side="left")
    title_label.bind("<Button-1>", lambda event: start_drag(window))

    def on_close():
        try:
            window.on_close()
        except AttributeError:
            pass

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
    global apps_offsetx, apps_offsety

    APP_HEIGHT = 120
    APP_WIDTH = 100

    app = ctk.CTkFrame(workspace, width=100, height=120, fg_color="transparent", bg_color="transparent")
    app.place(x=5+apps_offsetx, y=5+apps_offsety)
    image = ctk.CTkImage(pfp, pfp, (APP_WIDTH-5, APP_HEIGHT-30))

    p = ctk.CTkLabel(app, width=APP_WIDTH-5, height=APP_HEIGHT-30, text="", image=image)
    p.pack(padx=5, pady=2)

    title_label = ctk.CTkLabel(app, text=title, font=("monogram", 24), text_color="white")
    title_label.pack(padx=0, pady=0)

    def on_click(event):

        print("click")

        cmd(event)

    title_label.bind("<Button-1>", lambda event: on_click(event))
    p.bind("<Button-1>", lambda event: on_click(event))

    if workspace != None:
        if apps_offsety + APP_HEIGHT + 5 <= workspace.winfo_height():
            apps_offsety += APP_HEIGHT + 10
        else:
            apps_offsetx += APP_WIDTH + 5
            apps_offsety = 0

def to_image(image_path: str, size: tuple = (20,20), prefix: str = "images"):
    photo = Image.open(f"{prefix}/{image_path}")

    return photo

def update_loop():
    global dragging, counter, index
    global offset_x, offset_y 

    counter += 1

    if dragging:
        x, y = root.winfo_pointerxy()

        parent = dragging.master

        parent_x = parent.winfo_rootx()
        parent_y = parent.winfo_rooty()

        dragging.place(x=x - offset_x - parent_x, y=y - offset_y - parent_y)

    for v in todo:
        v()

    if counter == 5:
        counter = 0
        time_label.configure(text=f" {time.strftime("%H:%M:%S")} \n{time.strftime("%Y-%m-%d")[2:]}", text_color=colors[index])

        if len(colors) - 1 != index:
            index+=1
        else:
            index=0

    root.after(25, update_loop)