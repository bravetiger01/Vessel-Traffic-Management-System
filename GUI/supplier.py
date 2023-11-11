from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from datetime import *
import time
from tkintermapview import TkinterMapView

# -----------------------------------------------------------------------------
# ----------------------------------GUI----------------------------------------
# -----------------------------------------------------------------------------
root = Tk()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width,height))
root.resizable(False,False)
root.configure(bg='#ffffff')

# -----------------------------------------------------------------------------
# --------------------------------Functions------------------------------------
# -----------------------------------------------------------------------------
def show_time():
    Time = time.strftime("%H:%M:%S")
    Date = time.strftime('%Y:%m:%d')

    time_date_text = f"{Time} \n {Date}"

    date_time.configure(text=time_date_text, font=('', 13, 'bold'), bd=0, bg='white', fg='black')
    date_time.after(100, show_time)



# -----------------------------------------------------------------------------
# --------------------------------Dashboard------------------------------------
# -----------------------------------------------------------------------------

# ---------------------------------Header--------------------------------------
header = Frame(root, bg='#009df4')
header.place(x=300, y=0, width=int(width), height=int(height)//10)

logout = Button(header, text='Logout', bg='#32cf8e', font=('', 13, 'bold'), bd=0, fg='white', 
                cursor='hand2', activebackground='#32cf8e')
logout.place(x=1080, y=30)


# ---------------------------------Mapping--------------------------------------
map_frame = Frame(root, height = height, width=width//20)
map_frame.place(x=50, y=50)
map_widget = TkinterMapView(root, width=600, height=400
                            ,corner_radius=0)
map_widget.pack(fill='both', expand=True)

map_widget.set_position(-23.9759994293, -46.2888955111)
map_widget.set_zoom(100)

marker_1 = map_widget.set_marker(-23.9759994293, -46.2888955111, text= "PORT OF SANTOS, BRAZIL")


# ------------------------------------Sidebar----------------------------------------
sidebar = Frame(root, bg='#ffffff')
sidebar.place(x=0, y=0, height= height, width= width//5)


# ------------------------------------------------------------------------------------
# -------User--------
user_pic = Image.open(r"E:\Project CS\Vessel Traffic Management System\photos\user.png")
user_pic = user_pic.resize((int(width)//10,int(height)//5))
user_tkimg = ImageTk.PhotoImage(user_pic)

user_pic_label = Label(sidebar, image=user_tkimg, bg='#ffffff')
user_pic_label.place(x=75, y=10)

# Name of User
user_name = Label(sidebar, text='User', bg='#ffffff', font=('', 20, 'bold'))
user_name.place(x=120, y=200)
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# -----View Ships Icon-----
view_ships_pic = Image.open(r"E:\Project CS\Vessel Traffic Management System\photos\map-icon.png")
view_ships_pic = view_ships_pic.resize((50,50))
view_ships_tkimg = ImageTk.PhotoImage(view_ships_pic)

view_ships_pic_label = Label(sidebar, image=view_ships_tkimg, bg='#ffffff', cursor='hand2')
view_ships_pic_label.place(x=35, y=289)

# -----View Ships Button-----
view_ships_button = Button(sidebar, text='View Your Booked Ships', bg='#ffffff', bd=0, font=('', 10, 'bold'),
                           activebackground='#ffffff', cursor='hand2')
view_ships_button.place(x=100, y=312)
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# -----Book Ships Icon-----
book_ships_pic = Image.open(r"E:\Project CS\Vessel Traffic Management System\photos\booking.png")
book_ships_pic = book_ships_pic.resize((50,50))
book_ships_tkimg = ImageTk.PhotoImage(book_ships_pic)

book_ships_pic_label = Label(sidebar, image=book_ships_tkimg, bg='#ffffff', cursor='hand2')
book_ships_pic_label.place(x=35, y=370)

# -----Book Ships Button-----
book_ships_button = Button(sidebar, text='Book Our Ships', bg='#ffffff', bd=0, font=('', 10, 'bold'),
                           activebackground='#ffffff', cursor='hand2')
book_ships_button.place(x=100, y=390)
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# -------Time And Date-------
clock_pic = Image.open(r"E:\Project CS\Vessel Traffic Management System\photos\clock.png")
clock_pic = clock_pic.resize((50,50))
clock_tkimg = ImageTk.PhotoImage(clock_pic)

clock_pic_label = Label(sidebar, image=clock_tkimg, bg='#ffffff')
clock_pic_label.place(x= 35, y=(height)-100)

date_time = Label(root)
date_time.place(x=100, y= (height)-90)
show_time()

# ----------------------------------------------------------------------------------
# --------------------End-------------------
root.mainloop()