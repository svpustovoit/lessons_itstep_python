import tkinter as tk

root = tk.Tk()
root.title("GUI tkinter")
#root.iconbitmap("image.ico")
root.geometry("640x480")
root.resizable(True, True)
root.minsize(320, 240)
root.maxsize(1920, 1080)

label_title = tk.Label(master=root,
                       text="Hello Students!",
                       font=("Arial", 18, "bold italic"),
                       fg='#1B0CED',
                       bg='#FFC107',
                       width=20,
                       height=3,
                       anchor="center",  # n,e,s,w  ne,nw se, sw
                       relief="solid",  # solid,raised,sunken,flat,ridge,groove
                       bd=5,
                       justify="center", # CENTER,LEFT,RIGHT
                       )
label_title.pack()

button_play = tk.Button(master=root,
                        text="Click Me!",
                        font=("Arial", 18, "bold italic"),
                        fg='#1B0CED',
                        bg='#D65B0B',
                        width=30,
                        height=3,
                        anchor="center",
                        relief="solid",
                        )
button_play.pack()

img = tk.PhotoImage(file="pow.gif")
label_img = tk.Label(master=root,
                     image=img,
                     )
label_img.pack()

root.mainloop()
































