from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector as mysql
from datetime import *
import time

# ----------------MySQL Database-------------
# Connecting Database
def connect_to_database():
    db = mysql.connect(
        host="localhost",
        user="root",
        password="nakuldesai2510",
        database="vtms1"
    )
    return db

# ---------------------GUI-------------------
root = Tk()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.title('Vessel Traffic Managment System')
root.geometry('%dx%d+0+0' % (width,height))
root.resizable(False,False)
root.configure(bg='white')

# -------------------Designing----------------
signin_frame = Frame(root, width=width, height=height)
signin_frame.place(anchor='center', relx=0.5, rely=0.5)



# -------------Background---------------
# Backgound Image


background_img = Image.open(r"E:\Project CS\Vessel Traffic Management System\photos\loginphoto.jpg")
background_img = background_img.resize((width, height))
background_tkimg = ImageTk.PhotoImage(background_img)

bglabel = Label(signin_frame, image=background_tkimg)
bglabel.pack()


frame = Frame(signin_frame, width=350, height= 350, bg= 'white')
frame.place(x=600, y=270)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg= 'white', font= ('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# Sign In
def signin():
    username = user_name.get()
    key = password.get()
    # Verify admin credentials
    if verify_admin(username, key):
        messagebox.showinfo("Login Successful", "Admin login successful!")
        # Call admin menu function
        admin_menu()
        print(1)
    # Verify supplier credentials
    elif verify_supplier(username, key):
        messagebox.showinfo("Login Successful", "Supplier login successful!")
        # Call supplier menu function
        supplier_menu()
        print(2)

    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
        print(3)


# Admin login verification
def verify_admin(username, password):
    db = connect_to_database()
    cursor = db.cursor()
    query = "SELECT * FROM admin WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    db.close()
    return result is not None

# Supplier login verification
def verify_supplier(username, password):
    db = connect_to_database()
    cursor = db.cursor()
    query = "SELECT * FROM supplier WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    db.close()
    return result is not None

# -------------------------------Supplier------------------------------
def supplier_menu():
    signin_frame.destroy()
    supplier_frame = Frame(root)
    supplier_frame.pack()
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
    header = Frame(supplier_frame, bg='#009df4')
    header.place(x=300, y=0, width=int(width), height=int(height)//10)

    logout = Button(header, text='Logout', bg='#32cf8e', font=('', 13, 'bold'), bd=0, fg='white', 
                    cursor='hand2', activebackground='#32cf8e')
    logout.place(x=1080, y=30)


    # ------------------------------------Sidebar----------------------------------------
    sidebar = Frame(supplier_frame, bg='#ffffff')
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

    date_time = Label(supplier_frame)
    date_time.place(x=100, y= (height)-90)
    show_time()
    supplier_menu()

def admin_menu():
    pass


# Username
def on_enter(e):
    user_name.delete(0, 'end')
def on_leave(e):
    name = user_name.get()
    if name == '':
        user_name.insert(0, 'Username')


user_name = Entry(frame, width=25, fg='black',border=0 , bg='white', font=('Microsoft Yahei UI Light', 11))
user_name.place(x=30, y=80)
user_name.insert(0, 'Username')
user_name.bind('<FocusIn>', on_enter)
user_name.bind('<FocusOut>', on_leave)

Frame(frame, width = 295, height=2, bg='black').place(x=25, y=107)

# Password

def on_enter1(e):
    password.delete(0, 'end')
def on_leave1(e):
    name = password.get()
    if name == '':
        password.insert(0, 'Password')

password = Entry(frame, width=25, fg='black', border = 0, bg='white', font=('Microsoft Yahei UI Light', 11))
password.place(x=30, y=150)
password.insert(0, 'Password')
password.bind('<FocusIn>', on_enter1)
password.bind('<FocusOut>', on_leave1)

Frame(frame, width=295, height=2, border=0, bg='black').place(x=25, y=177)



# Button
Button(frame, width=39, pady=7, text='Sign In', command=signin, bg ='#57a1f8', fg= 'white', border=0).place(x=35, y=204)



# End
root.mainloop()