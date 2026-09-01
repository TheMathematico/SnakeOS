saved_text = "Type stuff here"
WIDTH = 500
HEIGHT = 500

def open(ctk, utility):
    global saved_text, WIDTH, HEIGHT

    saved_text = saved_text

    window = utility.create_window(WIDTH, HEIGHT, "Notes", fg="white", top_frame_fg="orange")

    textbox = ctk.CTkTextbox(window, width=WIDTH, height=HEIGHT, font=("monogram", 32), text_color="black", fg_color="white", border_width=0, corner_radius=0)
    textbox.insert("0.0", saved_text)
    textbox.pack(padx=0, pady=0)

    def close():
        global saved_text
        
        unsaved_text = textbox.get("0.0", "end-1c")

        saved_text = unsaved_text

    window.on_close = close




