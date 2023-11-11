from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector as mysql

# ----------------MySQL Database-------------
# Connecting Database
def connect_to_database():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="nakuldesai2510",
        database="vtms1"
    )
    return db

# ---------------------GUI-------------------
root = Tk()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width,height))
root.resizable(False,False)
root.configure(bg='white')

# -------------------Designing----------------


# -------------Background---------------
# Backgound Image
print(root.winfo_width())
print(root.winfo_height())

background_img = Image.open(r"E:\Project CS\Vessel Traffic Management System\loginphoto.jpg")
background_img = background_img.resize((root.winfo_screenwidth(),root.winfo_screenheight()))
background_tkimg = ImageTk.PhotoImage(background_img)

bglabel = Label(root, image=background_tkimg)
bglabel.place(x=0, y=0)


# img = PhotoImage(file='loginphoto.png')
# Label(root, image= img, bg='white').place(x=100, y=180)

frame = Frame(root, width=350, height= 350, bg= 'white')
frame.place(x=100, y=200)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg= 'white', font= ('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# Sign In
def signin():
    username = user_name.get()
    password = pass_word.get()

    print(username)
    print(password)

    if 'admin' in username:
        # Verify admin credentials
        if verify_admin(username, password):
            messagebox.showinfo("Login Successful", "Admin login successful!")
            # Call admin menu function
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
    # Verify supplier credentials
    else:
        if verify_supplier(username, password):
            messagebox.showinfo("Login Successful", "Supplier login successful!")
            # Call supplier menu function
            supplier_menu(username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")


# Admin login verification
def verify_admin(username, password):
    db = connect_to_database()
    cursor = db.cursor()
    query = "SELECT * FROM admin WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    db.close()
    return result is not None

def admin_menu():
    pass

# Supplier login verification
def verify_supplier(username, password):
    db = connect_to_database()
    cursor = db.cursor()
    query = "SELECT * FROM supplier WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    db.close()
    return result is not None

# --------------------------Supplier---------------------
def supplier_menu(username):
    pass


# Username
def on_enter():
    user_name.delete(0, 'end')
def on_leave():
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

def on_enter1():
    pass_word.delete(0, 'end')
def on_leave1():
    name = pass_word.get()
    if name == '':
        pass_word.insert(0, 'Password')

pass_word = Entry(frame, width=25, fg='black', border = 0, bg='white', font=('Microsoft Yahei UI Light', 11))
pass_word.place(x=30, y=150)
pass_word.insert(0, 'Password')
pass_word.bind('<FocusIn>', on_enter1)
pass_word.bind('<FocusOut>', on_leave1)

Frame(frame, width=295, height=2, border=0, bg='black').place(x=25, y=177)



# Button
Button(frame, width=39, pady=7, text='Sign In', command=signin, bg ='#57a1f8', fg= 'white', border=0).place(x=35, y=204)



# End
root.mainloop()