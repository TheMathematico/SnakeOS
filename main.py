import customtkinter as ctk
import utility
from apps import time
from apps import clicker
from PIL import Image
import pygame #for sound

ctk.set_appearance_mode("dark")
pygame.mixer.init()

WIDTH = 1500
HEIGHT = 920

tsk_bar_width = 100
TOP_FRAME_HEIGHT = 30

photo = Image.open("appdefault.png")
logo = Image.open("logo.png")
print(logo)
clock_icon = Image.open("clock.png")
cursor = Image.open("cursor.png")
clicker_icon = Image.open("clicker.png")

BACKGROUND = "#0B1F1A"
BACKGROUND_SECONDARY = "#14332A"
BACKGROUND_HOVER = "#1A3C34"

def on_close():
    root.destroy()

root = ctk.CTk(fg_color=BACKGROUND)
root.geometry(f"{WIDTH}x{HEIGHT}")
root.title("Snake OS")

click_sound = pygame.mixer.Sound("click.mp3")

def on_click(event):
    click_sound.play()

root.bind_all("<Button-1>", on_click)

background = ctk.CTkImage(logo, logo, (200, 200))

taskbar = ctk.CTkFrame(root, width=tsk_bar_width, height=HEIGHT-20, fg_color=BACKGROUND_SECONDARY, corner_radius=15)
taskbar.place(x=0+10, y=10)
taskbar.pack_propagate(False)

workspace = ctk.CTkLabel(root, width=WIDTH-tsk_bar_width-30, height=HEIGHT-20, fg_color=BACKGROUND_SECONDARY, corner_radius=15, text="", image=background)
workspace.place(x=tsk_bar_width + 20, y=10)

utility.workspace = workspace
utility.root = root
utility.TOP_FRAME_HEIGHT = TOP_FRAME_HEIGHT
utility.BACKGROUND = BACKGROUND
#background_hover isn't assigned because it is already assigned in utility
utility.BACKGROUND_SECONDARY = BACKGROUND_SECONDARY

close = utility.add_button(taskbar, 80, tsk_bar_width-4, "shutdown", 22, on_close, BACKGROUND_SECONDARY, BACKGROUND_HOVER, 10, "bottom")
asjdlasd = utility.add_button(taskbar, 80, tsk_bar_width-4, "+", 32, lambda: utility.create_window(300, 300, "test", BACKGROUND_HOVER), BACKGROUND_SECONDARY, BACKGROUND_HOVER, 0, "bottom")

utility.create_app("time", clock_icon, lambda event: time.open())
utility.create_app("ZooClicker", clicker_icon, lambda event: clicker.open(cursor, BACKGROUND_SECONDARY))
utility.create_app("uno", photo, lambda event: utility.create_window(500, 500, "uno"))

utility.update_loop()

root.mainloop()