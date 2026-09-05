import customtkinter as ctk

w = 350
h = 400

def start_test(time, btn, status_label):
    status_label.configure(text="Focus, green=click")
    btn.configure(fg_color="red", hover_color="red")

    #this many funcs inside 1 func seems unclean but being totally honest i don't know any solution
    def test():
        start = time.monotonic()
        end = 0

        def set():
            end = time.monotonic()
            interval = int(round(end-start, 3) * 1000)
            status_label.configure(text=f"{interval}ms, click to retry")
            btn.configure(fg_color="orange", hover_color="yellow", command=lambda: start_test(time, btn, status_label))

        btn.configure(fg_color="green", hover_color="green", command=set)
        status_label.configure(text="CLICK!")

    btn.after(1500, test)

def open(a, time, utility):
    global w,h

    window = utility.create_window(w, h, "Admin")

    status_label = ctk.CTkLabel(window, text="Click when ready", font=("monogram", 24))
    status_label.pack(padx=0, pady=0)

    btn = ctk.CTkButton(
        window, 
        width=w-10, 
        height=h-30,
        text="", 
        fg_color="orange", 
        hover_color="yellow",
        command=lambda: start_test(time, btn, status_label)
    )                        
    btn.pack(padx=2, pady=5, side="bottom")