import customtkinter as ctk
import utility
from apps import time
from PIL import Image

ctk.set_appearance_mode("dark")

WIDTH = 1500
HEIGHT = 920

tsk_bar_width = 100
TOP_FRAME_HEIGHT = 30

photo = Image.open("appdefault.png")
clock_icon = Image.open("clock_icon.png")

BACKGROUND = "#0B1F1A"
BACKGROUND_SECONDARY = "#14332A"
BACKGROUND_HOVER = "#1A3C34"

def on_close():
    root.destroy()

root = ctk.CTk(fg_color=BACKGROUND)
root.geometry(f"{WIDTH}x{HEIGHT}")
root.title("Snake OS")

taskbar = ctk.CTkFrame(root, width=tsk_bar_width, height=HEIGHT-20, fg_color=BACKGROUND_SECONDARY, corner_radius=15)
taskbar.place(x=0+10, y=10)
taskbar.pack_propagate(False)

workspace = ctk.CTkFrame(root, width=WIDTH-tsk_bar_width-30, height=HEIGHT-20, fg_color=BACKGROUND_SECONDARY, corner_radius=15)
workspace.place(x=tsk_bar_width + 20, y=10)

utility.workspace = workspace
utility.root = root
utility.TOP_FRAME_HEIGHT = TOP_FRAME_HEIGHT
utility.BACKGROUND = BACKGROUND
utility.BACKGROUND_HOVER = BACKGROUND_HOVER
utility.BACKGROUND_SECONDARY = BACKGROUND_SECONDARY

close = utility.add_button(taskbar, 80, tsk_bar_width-4, "shutdown", 22, on_close, BACKGROUND_SECONDARY, BACKGROUND_HOVER, 10, "bottom")
asjdlasd = utility.add_button(taskbar, 80, tsk_bar_width-4, "+", 32, lambda: utility.create_window(300, 300, "test", BACKGROUND_HOVER), BACKGROUND_SECONDARY, BACKGROUND_HOVER, 0, "bottom")

utility.create_app("time", clock_icon, lambda event: time.open())
utility.create_app("clicker", photo, lambda event: utility.create_window(100, 200, "clicker", 0))
utility.create_app("uno", photo, lambda event: utility.create_window(500, 500, "uno", 0))

utility.update_loop()

root.mainloop()