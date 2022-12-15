from Client.Frames import Frame
import tkinter as tk


def Main():
    root = tk.Tk()
    root.title("Conversor de monedas")
    app = Frame(root)
    root.mainloop()

    for child in app.winfo_children():
        child.grid_configure(padx=5, pady=5)





if __name__ == '__main__':
    Main()

