from tkinter import *
from Ventana import *


def main():
    root=Tk()
    root.wm_title("Inventario")
    img=PhotoImage(file="data.png")
    root.iconphoto(False,img)
    app = Ventana(root)
    app.mainloop()
    

if __name__ == "__main__":
    main()