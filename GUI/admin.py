from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# ---------------------GUI-------------------
root = Tk()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width,height))
root.resizable(False,False)
root.configure(bg='white')



# --------------------End-------------------
root.mainloop()