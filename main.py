import customtkinter as ctk
import utility
import time
from apps import time_app, clicker, admin, notes, reaction_time
import pygame #for sound

ctk.set_appearance_mode("dark")
pygame.mixer.init()

WIDTH = 1500
HEIGHT = 920

tsk_bar_width = 100
TOP_FRAME_HEIGHT = 30

photo = utility.to_image("appdefault.png")
logo = utility.to_image("logo.png")
clock_icon = utility.to_image("clock.png")
cursor = utility.to_image("cursor.png")
clicker_icon = utility.to_image("clicker.png")
admin_icon = utility.to_image("admin.png")
notes_icon = utility.to_image("notepad.png")
retime_icon = utility.to_image("retime.png")

BACKGROUND = utility.BACKGROUND
BACKGROUND_SECONDARY = utility.BACKGROUND_SECONDARY
BACKGROUND_HOVER = utility.BACKGROUND_HOVER

def on_close():
    root.destroy()

root = ctk.CTk(fg_color=BACKGROUND)
root.geometry(f"{WIDTH}x{HEIGHT}")
root.title("Snake OS")

click_sound = pygame.mixer.Sound("sounds/click.mp3")
click_sound.set_volume(0.25)

def on_click(event):
    click_sound.play()

root.bind_all("<Button-1>", on_click)

background = ctk.CTkImage(logo, logo, (200, 200))

taskbar = ctk.CTkFrame(root, width=tsk_bar_width, height=HEIGHT-20, fg_color=BACKGROUND_SECONDARY, corner_radius=15)
taskbar.place(x=0+10, y=10)
taskbar.pack_propagate(False)

workspace = ctk.CTkLabel(root, width=WIDTH-tsk_bar_width-30, height=HEIGHT-20, fg_color=BACKGROUND_SECONDARY, corner_radius=15, text="", image=background)
workspace.place(x=tsk_bar_width + 20, y=10)
workspace.update_idletasks() #This line is here so that ctk calculates the geometry of workspace(since for some reason it doesn't automatically, at least quick enough)
                             #because create_app needs the height of workspace so that it can
                             #organize the apps properly
utility.workspace = workspace
utility.root = root
utility.TOP_FRAME_HEIGHT = TOP_FRAME_HEIGHT

#taskbar related widgets
close = utility.add_button(taskbar, 40, tsk_bar_width-4, "⏻", 22, on_close, pad=10, tc="green")

time_label = ctk.CTkLabel(taskbar, text="00:00", font=("monogram", 24))
time_label.pack(padx=0, pady=10)
utility.time_label = time_label

#workspace related apps
utility.create_app("Time", clock_icon, lambda event: time_app.open(utility, ctk))
utility.create_app("ZooClicker", clicker_icon, lambda event: clicker.open(cursor, BACKGROUND_SECONDARY, ctk, utility))
utility.create_app("Admin", admin_icon, lambda event: admin.open(clicker, ctk, utility))
utility.create_app("Notes", notes_icon, lambda event: notes.open(ctk, utility))
utility.create_app("ReTime", retime_icon, lambda event: reaction_time.open(ctk, time, utility))

utility.update_loop()

root.mainloop()