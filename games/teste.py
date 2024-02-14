import tkinter as tk

root = tk.Tk()
root.title("Exemplo Tkinter")

label = tk.Label(root, text="Olá, mundo!")
label.pack()

root.mainloop()