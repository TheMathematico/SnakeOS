import customtkinter as ctk
import utility

w = 500
h = 500

horizontal_offset = 5
vertical_offset = 5

assignable_height = 50
assignable_width = w - horizontal_offset * 2

def create_assignable(parent, variable, module, name, fg, rainbow = False):
    print("called")
    global assignable_height, assignable_width, horizontal_offset, vertical_offset

    frame = ctk.CTkFrame(parent, width=assignable_width, height=assignable_height, fg_color=fg)
    frame.pack(padx=horizontal_offset, pady=vertical_offset, anchor="n")
    frame.pack_propagate(False)

    variable_type = type(variable).__name__

    title = ctk.CTkLabel(frame, text=f"{name}, type: {variable_type}", font=("monogram", 32))
    title.pack(padx=horizontal_offset, pady=0, side="left")

    def submit():
        nonlocal entry, submit_button
        nonlocal variable, variable_type

        try:
            print('yes')

            if variable_type != "int":
                print("banan")
                change = entry.get()
            else:
                print("yabloko")
                change = int(entry.get())

            setattr(module, name, change)
            submit_button.configure(fg_color="lime")
            parent.after(250, submit_button.configure(fg_color="green"))
        except Exception:
            print('bruh')
            submit_button.configure(fg_color="red")
            parent.after(250, submit_button.configure(fg_color="green"))


    submit_button = ctk.CTkButton(
        frame, 
        width=50, 
        height=45, 
        text="✔", 
        font=("monogram", 32), 
        fg_color="green",
        hover_color=utility.BACKGROUND_HOVER,
        command=submit
    )
    submit_button.pack(padx=horizontal_offset, pady=0, side="right")

    entry = ctk.CTkEntry(
        frame, 
        width=int(assignable_width/3),
        height=assignable_height-vertical_offset,
        placeholder_text=f"Set {name}",
    )
    entry.pack(padx=0, pady=0, side="right") #0 padx because submit_button already has the offset both left and right

    print(frame)

def open(clicker):
    global w,h

    window = utility.create_window(w, h, "Admin")

    title = ctk.CTkLabel(window, text="Evil cheatsheet >:(", font=("monogram", 32))
    title.pack(padx=0, pady=0, anchor="n")

    create_assignable(window, clicker.clicks, clicker, "clicks", utility.BACKGROUND_SECONDARY)
    create_assignable(window, clicker.clicks, clicker, "clicks_add", utility.BACKGROUND_SECONDARY)
    create_assignable(window, clicker.clicks, clicker, "income_delay", utility.BACKGROUND_SECONDARY)
