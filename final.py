from tkinter import *
from tkinter import messagebox
from tkintermapview import TkinterMapView
from PIL import ImageTk, Image
import mysql.connector as connector
from datetime import *
import time
from tkinter import ttk
from tkinter import messagebox
import random
from customtkinter import *
from tkcalendar import DateEntry
from datetime import datetime, timedelta

# ----------------------------------------------------------------MySQL Database----------------------------------------------------------
# Connecting Database
def connect_to_database():
    db = connector.connect(host="localhost", user="root", password="nakuldesai2510",database="vtms")

    return db

# --------------------------------------------------------------------Ships---------------------------------------------------------------
class Ships:
    speed = 0
    # IMO Number = The International Maritime Organization (IMO) number uniquely identifies each seagoing ship. It is an important reference for tracking and managing vessels.
    def __init__(self, name, IMO_Number , condition, capacity, navigation_status, type, Embarkation,departuretime,Destination,arrivaltime, imagelocation, bookingstatus):
        self.Name = name
        self.Condition = condition
        self.Navigation_Status = navigation_status
        self.IMO_Number = IMO_Number
        self.Type = type
        self.Embarkation = Embarkation
        self.Departure_Time = departuretime
        self.Destination = Destination
        self.Arrival_Time = arrivaltime
        self.Image_Location = imagelocation
        self.Capacity = capacity
        self.BookingStatus = bookingstatus

    @classmethod
    def change_condition(cls, condition):
        cls.condition = condition
    
    @classmethod
    def change_navigation_status(cls, navigation_status):
        cls.navigation_status = navigation_status

    def update_speed(self):
        self.speed = random.randint(25, 30)


# ---------------------GUI-------------------
root = Tk()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.title('Vessel Traffic Managment System')
root.geometry('%dx%d+0+0' % (width,height))
root.configure(bg='white')
global check_and_update_navigation_status

# -------------------Designing----------------


# admin_frame = Frame(root, width=width, height=height)
# supplier_frame = Frame(root, width=width, height=height)

background_img = Image.open(r"E:\Project CS\Vessel Traffic Management System\GUI\photos\loginphoto.jpg")
background_img = background_img.resize((width, height))
background_tkimg = ImageTk.PhotoImage(background_img)





# -----------------------------------------------------------------SIGN IN WINDOW---------------------------------------------------------
def signin_window():
    global signin_frame, user_name, pass_word,showpassword
    signin_frame = Frame(root, width=width, height=height)
    signin_frame.place(anchor='center', relx=0.5, rely=0.5)
    print(1)

    showpassword = True

    # Username
    def on_enter(e):
        global user_name
        if user_name.get() == 'Username':
            user_name.delete(0, 'end')
        else:
            pass
    def on_leave(e):
        global user_name
        name = user_name.get()
        if name == '':
            user_name.insert(0, 'Username')

    def on_enter1(e):
        global pass_word,showpassword
        if pass_word.get() == 'Password':
            pass_word.delete(0, 'end')
            pass_word.config(show='*')
        else:
            if showpassword == True:
                pass_word.config(show='*')
            else:
                pass_word.config(show='')
    def on_leave1(e):
        global pass_word,showpassword
        name = pass_word.get()
        if name == '':
            pass_word.insert(0, 'Password')
            pass_word.config(show='')
        else:
            if showpassword == True:
                pass_word.config(show='*')
            else:   
                pass_word.config(show='')
    

    bglabel = Label(signin_frame, image=background_tkimg)
    bglabel.pack()


    frame = Frame(signin_frame, width=350, height= 350, bg= 'white')
    frame.place(x=600, y=270)

    heading = Label(frame, text='Sign in', fg='#57a1f8', bg= 'white', font= ('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    # Sign In
    def signin():
        username = user_name.get()
        key = pass_word.get()
        # Verify admin credentials
        if 'admin' in username:
            if verify_admin(username, key):
                messagebox.showinfo("Login Successful", "Admin login successful!")
                # Call admin menu function
                admin_menu()
                print(1)
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")
                print(3)
        else:
            # Verify supplier credentials
            if verify_supplier(username, key):
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
        cursor.execute("select * from authentication")
        result = cursor.fetchall()
        for data in result:
            if data[0] == username and data[1] == password:
                db.close()
                return result is not None
            else:
                pass
        else:
            return result is None

    # Supplier login verification
    def verify_supplier(username, password):
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute("select * from authentication")
        result = cursor.fetchall()
        for data in result:
            if data[0] == username and data[1] == password:
                db.close()
                return result is not None
            else:
                pass
        else:
            return result is None
    
    def show_password():
        global showpassword
        showpassword = True
        if pass_word.get() == 'Password':
            pass
        else:
            if pass_word.cget('show') == '*':
                pass_word.config(show='')
            else:
                pass_word.config(show='*')
    
    pass_word = Entry(frame,width=25,show='*',fg='black',border = 0,bg='white',font=('Microsoft Yahei UI Light', 11))
    pass_word.place(x=30, y=150)
    pass_word.insert(0, 'Password')
    if pass_word.get()== 'Password':
        pass_word.config(show='')
    else:
        pass_word.config(show='*')
    pass_word.bind('<FocusIn>', on_enter1)
    pass_word.bind('<FocusOut>', on_leave1)

    check_button = Checkbutton(frame, text='Show Password', command=show_password)
    check_button.place(x=25, y=200)
    

    user_name = Entry(frame, width=25, fg='black',border=0 , bg='white', font=('Microsoft Yahei UI Light', 11))
    user_name.place(x=30, y=80)
    user_name.insert(0, 'Username')
    user_name.bind('<FocusIn>', on_enter)
    user_name.bind('<FocusOut>', on_leave)

    Frame(frame, width = 295, height=2, bg='black').place(x=25, y=107)
    # Password
    Frame(frame, width=295, height=2, border=0, bg='black').place(x=25, y=177)

    # Button
    Button(frame, width=39, pady=7, text='Sign In', command=signin, bg ='#57a1f8', fg= 'white', border=0).place(x=35, y=300)

# ------------------------------------------------Supplier-------------------------------------------
user_pic = Image.open(r"GUI\photos\user.png")
user_pic = user_pic.resize((int(width)//10,int(height)//5))
user_tkimg = ImageTk.PhotoImage(user_pic)

# -----View Ships Icon-----
view_ships_pic = Image.open(r"E:\Project CS\Vessel Traffic Management System\GUI\photos\map-icon.png")
view_ships_pic = view_ships_pic.resize((50,50))
view_ships_tkimg = ImageTk.PhotoImage(view_ships_pic)

# -----Book Ships Icon-----
book_ships_pic = Image.open(r"E:\Project CS\Vessel Traffic Management System\GUI\photos\booking.png")
book_ships_pic = book_ships_pic.resize((50,50))
book_ships_tkimg = ImageTk.PhotoImage(book_ships_pic)


# -------Time And Date-------
clock_pic = Image.open(r"E:\Project CS\Vessel Traffic Management System\GUI\photos\clock.png")
clock_pic = clock_pic.resize((50,50))
clock_tkimg = ImageTk.PhotoImage(clock_pic)

# Logout Button
logout_btn_pic = Image.open(r"E:\Project CS\Vessel Traffic Management System\GUI\photos\logout.png")
logout_btn_pic = logout_btn_pic.resize((50,50))
logout_btn_tkimg = CTkImage(logout_btn_pic)

def logout():
    global frame1
    try:
        frame1.destroy()
    except:
        supplier_frame.destroy()
    finally:
        signin_window()
    

# ---------------------------------------------------------------Supplier Menu-----------------------------------------------------------
def supplier_menu():
    global signin_frame,user_tkimg,clock_tkimg,background_tkimg,book_ships_tkimg,view_ships_tkimg,ship_image_tk_list,supplier_frame
    signin_frame.destroy()
    supplier_frame = Frame(root, width=width, height=height)
    supplier_frame.pack(fill=BOTH, expand=True)
    # At the beginning of your script
    ship_image_tk_list = []
    # Fetch ship data from the database
    def fetch_ship_data():
        db = connect_to_database()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM SHIPDATA")
        data = cursor.fetchall()
        db.close()
        return data

    def fetch_booked_ships():
        db = connect_to_database()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM SHIPDATA WHERE BookingStatus = 'BOOKED'")
        data = cursor.fetchall()
        db.close()
        return data


    def show_time():
        Time = time.strftime("%H:%M:%S")
        Date = time.strftime('%Y:%m:%d')

        time_date_text = f"{Time} \n {Date}"

        date_time.configure(text=time_date_text, font=('', 13, 'bold'), bd=0, bg='white', fg='black')
        date_time.after(100, show_time)

    def view_ship():
        view_ship_frame = Frame(main_frame)
        view_ship_frame.pack(pady=20)

        
        # Create a canvas for the scrollable area
        canvas = Canvas(view_ship_frame, bg='#ffffff', width=1200, height=height)
        canvas.pack(side="left", fill="both", expand=True)

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(view_ship_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas
        frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw", width=1200, height=height+height)
        # Bind the canvas to the scrollbar
        frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        def display_ship_card(ship_data, row, column):
            global ship_image_tk_list
            card_frame = ttk.Frame(frame, borderwidth=2, relief="solid", width=1200, height=600)
            card_frame.grid(row=row, column=column, padx=50, pady=30)

            # Ship image
            ship_image = Image.open(ship_data.Image_Location)
            ship_image = ship_image.resize((1000,500))  # Adjust the size as needed
            ship_image_tk_list.append(ImageTk.PhotoImage(ship_image))

            Label(card_frame, image=ship_image_tk_list[-1], width=500).grid(row=0, column=0, columnspan=2, pady=5)

            # Ship name and Embarkation
            Label(card_frame, text=f"Ship: {ship_data.Name}", width=60).grid(row=1, column=1, sticky="w")
            Label(card_frame, text=f"Type: {ship_data.Type}", width=60).grid(row=2, column=1, sticky="w")
            Label(card_frame, text=f"Capacity: {ship_data.Capacity}", width=60).grid(row=3, column=1, sticky="w")
            Label(card_frame, text=f"Embarkation: {ship_data.Embarkation}", width=60).grid(row=4, column=1, sticky="w")
            Label(card_frame, text=f"Destination: {ship_data.Destination}", width=60).grid(row=5, column=1, sticky="w")

            # Display booking status
            if ship_data.BookingStatus == "BOOKED":
                Label(card_frame, text="Booking Status: BOOKED", fg="green", width=60).grid(row=6, column=0, columnspan=2, pady=5)
            else:
                Label(card_frame, text="Booking Status: NOT BOOKED", fg="red", width=60).grid(row=6, column=0, columnspan=2, pady=5)
        
        # Create instances of the Ships class from the fetched data
        ships_data = fetch_booked_ships()
        ships_instances = [Ships(name=ship["Name"], IMO_Number=ship["IMO"], condition=ship["Condition"],
                                capacity=ship["Capacity"], navigation_status=ship["Navigation_Status"],
                                type=ship["TYPE"], Embarkation=ship["Embarkation"], departuretime=ship["Departure_Time"],
                                Destination=ship["Destination"], arrivaltime=ship["Arrival_Time"],
                                imagelocation=ship["Image"], bookingstatus=ship["BookingStatus"]) for ship in ships_data]

        # Display Ship Card
        for i, ship_instance in enumerate(ships_instances):
            display_ship_card(ship_instance, i // 2, i % 2)


    # Function to book a ship
    def book_this_ship(ship_data):
        # Implement your logic to book the ship
        print(f"Booking ship: {ship_data.Name}")
        ship_data.BookingStatus = 'BOOKED'
        db = connect_to_database()
        csor = db.cursor()
        csor.execute(f"UPDATE SHIPDATA SET Name = '{ship_data.Name}',TYPE = '{ship_data.Type}',IMO = {ship_data.IMO_Number},Capacity = {ship_data.Capacity},`Condition` = '{ship_data.Condition}',Navigation_Status = '{ship_data.Navigation_Status}',Embarkation = '{ship_data.Embarkation}',Departure_Time = '{ship_data.Departure_Time}',Destination = '{ship_data.Destination}',Arrival_Time = '{ship_data.Arrival_Time}',Image = '{ship_data.Image_Location}',BookingStatus = '{ship_data.BookingStatus}' WHERE IMO = {ship_data.IMO_Number}")
        db.commit()
        indicate(view_ships_indicator, view_ship)
        
    def book_ship():
        book_ship_frame = Frame(main_frame)
        book_ship_frame.pack(pady=20)

        # Fetch all ships
        ships_data = fetch_ship_data()

        # Create a canvas for the scrollable area
        canvas = Canvas(book_ship_frame, bg='#ffffff', width=1200, height=height)
        canvas.pack(side="left", fill="both", expand=True, anchor='w')

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(book_ship_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas
        frame2 = Frame(canvas, highlightbackground='black', highlightthickness=2)
        canvas.create_window((0, 0), window=frame2, anchor="nw", width=1800, height=(height+height))
        # Bind the canvas to the scrollbar
        frame2.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        def display_ship_card(ship_data, row, column):
            print("Displaying ship data:", ship_data)
            card_frame = Frame(frame2, borderwidth=5, width=1400, height=400,relief='groove',highlightthickness=2)
            card_frame.grid(row=row,column=column,pady=10, columnspan=15)

            if ship_data.BookingStatus == 'NOT BOOKED':
                card_frame.grid_configure(padx=10)

            # Ship image
            ship_image = Image.open(ship_data.Image_Location)
            ship_image = ship_image.resize((800, 400))  # Adjust the size as needed
            ship_image_tk_list.append(ImageTk.PhotoImage(ship_image))

            Label(card_frame, image=ship_image_tk_list[-1], width=400).grid(row=0,column=0,pady=5, rowspan=6)

            # Ship name and Embarkation
            Label(card_frame, text=f"Ship: {ship_data.Name}", font=('Bold', 16)).grid(row=0, column=2, sticky="w")
            Label(card_frame, text=f"Embarkation: {ship_data.Embarkation}", font=('Bold', 12)).grid(row=1, column=2, sticky="w")

            # Display all details
            Label(card_frame, text=f"IMO Number: {ship_data.IMO_Number}", font=('Bold', 12)).grid(row=1, column=1, sticky="w",padx=1)
            Label(card_frame, text=f"Type: {ship_data.Type}", font=('Bold', 12)).grid(row=2, column=1, sticky="w",padx=1)
            Label(card_frame, text=f"Condition: {ship_data.Condition}", font=('Bold', 12)).grid(row=3, column=1, sticky="w",padx=1)
            Label(card_frame, text=f"Capacity: {ship_data.Capacity}", font=('Bold', 12)).grid(row=3, column=2, sticky="w",padx=1)
            Label(card_frame, text=f"Destination: {ship_data.Destination}", font=('Bold', 12)).grid(row=2, column=2, sticky="w",padx=1)
            Label(card_frame, text=f"Departure Time: {ship_data.Departure_Time}", font=('Bold', 12)).grid(row=1, column=3, sticky="w",padx=1)
            Label(card_frame, text=f"Arrival Time: {ship_data.Arrival_Time}", font=('Bold', 12)).grid(row=2, column=3, sticky="w",padx=1)
            Label(card_frame, text=f"Navigation Status: {ship_data.Navigation_Status}", font=('Bold', 12)).grid(row=3, column=3, sticky="w",padx=1)
            # If the ship is not booked, show the book button
            if ship_data.BookingStatus== 'BOOKED':
                Label(card_frame, text=f"Booking Status: \b\b\b{ship_data.BookingStatus}", font=('Bold', 12)).grid(row=4, column=2, sticky="w",padx=1)

            else:
                book_button = CTkButton(card_frame, text="Book Ship", command=lambda: book_this_ship(ship_data))
                book_button.grid(row=5,column=2)
                Label(card_frame, text=f"Booking Status: {ship_data.BookingStatus}", font=('Bold', 12)).grid(row=4, column=2, sticky="w",padx=1)

        ships_instances = [Ships(name=ship["Name"], IMO_Number=ship["IMO"], condition=ship["Condition"],
                                capacity=ship["Capacity"], navigation_status=ship["Navigation_Status"],
                                type=ship["TYPE"], Embarkation=ship["Embarkation"], departuretime=ship["Departure_Time"],
                                Destination=ship["Destination"], arrivaltime=ship["Arrival_Time"],
                                imagelocation=ship["Image"], bookingstatus=ship["BookingStatus"]) for ship in ships_data]
        
        print("Number of ships instances:", len(ships_instances))
        # Display Ship Card
        for i, ship_instance in enumerate(ships_instances):
            display_ship_card(ship_instance, i, 0)


    def hide_indicators():
        view_ships_indicator.config(bg='#ffffff')
        book_ships_indicator.config(bg='#ffffff')

    def delete_pages():
        for frame in main_frame.winfo_children():
            if frame == header:
                continue
            else:
                frame.destroy()

    def indicate(lb, page):
        hide_indicators()
        lb.config(bg='#158aff')
        delete_pages()
        page()

    # -----------------------------------------------------------------------------
    # --------------------------------Dashboard------------------------------------
    # -----------------------------------------------------------------------------

    # ------------------------------------Sidebar----------------------------------------
    sidebar = Frame(supplier_frame,bg='#ffffff',height=height,width=(width//5)-15)
    sidebar.pack(side=LEFT)
    sidebar.pack_propagate(False)

    # ---------------------------------Header--------------------------------------
    # ---------------------------------------------------------------Main Frame---------------------------------------------------------------
    main_frame = Frame(supplier_frame, highlightbackground='black', highlightthickness=2, width=width, height=height)
    main_frame.pack(side=LEFT)
    main_frame.pack_propagate(False)

    header = Frame(main_frame, bg='#009df4', width=width, height=(height//10)-10)
    header.pack()

    logoutbtn = Button(header, text='Logout',bg='#32cf8e',font=('', 13, 'bold'),bd=0,fg='white',cursor='hand2',activebackground='#32cf8e',command=logout)
    logoutbtn.place(x=1080, y=30)

    # ------------------------------------------------------------------------------------
    # -------User--------
    

    user_pic_label = Label(sidebar, image=user_tkimg, bg='#ffffff')
    user_pic_label.place(x=75, y=10)

    # Name of User
    user_name = Label(sidebar, text='User', bg='#ffffff', font=('Helvatica', 20, 'bold'))
    user_name.place(x=120, y=200)
    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    # -----View Ships Icon-----
    view_ships_pic = Image.open(r"E:\Project CS\Vessel Traffic Management System\photos\map-icon.png")
    view_ships_pic = view_ships_pic.resize((50,50))
    view_ships_tkimg = ImageTk.PhotoImage(view_ships_pic)

    view_ships_pic_label = Label(sidebar, image=view_ships_tkimg, bg='#ffffff',fg='#158aff' ,cursor='hand2')
    view_ships_pic_label.place(x=35, y=289)

    # -----View Ships Button-----
    view_ships_button = Button(sidebar, text='View Your Booked Ships', bg='#ffffff',fg='#158aff' ,bd=0, font=('', 10, 'bold'), cursor='hand2'
                            ,command=lambda: indicate(view_ships_indicator, view_ship))
    view_ships_button.place(x=100, y=312)

    view_ships_indicator = Label(sidebar, text='', bg='#ffffff')
    view_ships_indicator.place(x=20, y=300, width=5, height=50)
    # ----------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------
    # -----Book Ships Icon-----
    book_ships_pic = Image.open(r"E:\Project CS\Vessel Traffic Management System\photos\booking.png")
    book_ships_pic = book_ships_pic.resize((50,50))
    book_ships_tkimg = ImageTk.PhotoImage(book_ships_pic)

    book_ships_pic_label = Label(sidebar, image=book_ships_tkimg, bg='#ffffff', cursor='hand2')
    book_ships_pic_label.place(x=35, y=370)

    # -----Book Ships Button-----
    book_ships_button = Button(sidebar, text='Book Our Ships', bg='#ffffff',fg='#158aff',bd=0, font=('', 10, 'bold'),
                            activebackground='#ffffff', cursor='hand2'
                            ,command=lambda: indicate(book_ships_indicator, book_ship))
    book_ships_button.place(x=100, y=390)

    book_ships_indicator = Label(sidebar, text='', bg='#ffffff')
    book_ships_indicator.place(x=20, y=380, width=5, height=50)

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
    indicate(view_ships_indicator, view_ship)
    show_time()

# ----------------------------------------------------------------Admin Menu-------------------------------------------------------------
def admin_menu():
    global frame1,signin_frame,my_tree,logoutbtn,check_and_update_navigation_status
    signin_frame.destroy()
    db = connect_to_database()
    csor = db.cursor()
    frame1 = CTkFrame(master=root,width=width,height=height)
    frame1.pack(fill=BOTH,expand=True)

    logoutbtn = CTkButton(master=frame1,text='',image=logout_btn_tkimg,width=50,height=50,command=logout)
    logoutbtn.pack(side=TOP,anchor=NW,padx=5,pady=5)

    dataframe = None

    def upload_image():
        global file_path
        file_path = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        
        # Do something with the file_path (display it, save it, etc.)
        print("Selected File:", file_path)
        Add_Entry()

    def Add_Entry():
        global image_path_entry, file_path
        image_path_entry.delete(0, END)
        image_path_entry.insert(0, file_path)


    # ---------------------------------------------Data Showing-------------------------------------------
    def mainthing(x):
        global dataframe,my_tree,image_path_entry,my_tree
        if x == 'show':
            dataframe = CTkFrame(master=frame1,width=450,height=1000,
                            corner_radius=15,border_width=2)

            dataframe.place(relx=0.5, rely=0.5, anchor=CENTER)
            dataframe.pack_configure(expand=True,padx=5)
            # -----------------------------Treeview------------------------------------
            # Style
            style = ttk.Style()

            # Theme
            style.theme_use('clam')

            # Treeiew colors
            style.configure('Custom.Treeview',
                            background='#1E1E1E',
                            fieldbackground='#2D2D2D',
                            foreground ='#FFFFFF',
                            rowheight = 30,
                            )

            style.configure('Custom.Tkinter', highlightthickness=0, bd=0)

            style.configure("Treeview.Heading", background="#2D2D2D", foreground="#FFFFFF")
            style.configure("Custom.Treeview.Treeitem", background='#2D2D2D')

            # Changing selescted entry colour
            style.map('Treeview',
                    background=[('selected', '#3A3A3A')])

            # Treeview Frame
            tree_frame = Frame(dataframe)
            tree_frame.pack(padx=10, pady=15)

            # Treeview Scrollbar
            tree_scroll = Scrollbar(tree_frame)
            tree_scroll.pack(side=RIGHT, fill=Y)

            # --------------Treeview--------------
            my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended', style='Custom.Treeview')
            my_tree.pack()

            # Configuring Scrollbar
            tree_scroll.config(command=my_tree.yview)

            # Defining Columns
            my_tree['columns'] = ('Name','Type','IMO','Capacity','Condition','Navigation Status','Embarkation','Departure Time','Destination','Arrival Time','Image Location', 'BookingStatus')

            # Formating Columns
            my_tree.column('#0', width=0, stretch=NO)
            my_tree.column('Name', anchor=CENTER, width=110)
            my_tree.column('Type', anchor=CENTER, width=110)
            my_tree.column('IMO', anchor=CENTER, width=110)
            my_tree.column('Capacity', anchor=CENTER, width=100)
            my_tree.column('Condition', anchor=CENTER, width=110)
            my_tree.column('Navigation Status', anchor=CENTER, width=110)
            my_tree.column('Embarkation', anchor=CENTER, width=100)
            my_tree.column('Departure Time', anchor=CENTER, width=100)
            my_tree.column('Destination', anchor=CENTER, width=100)
            my_tree.column('Arrival Time', anchor=CENTER, width=100)
            my_tree.column('Image Location', anchor=CENTER, width=90)
            my_tree.column('BookingStatus', anchor=CENTER, width=90)


            # Creating Heading
            my_tree.heading('#0', text='', anchor=W)
            my_tree.heading('Name', text='Name', anchor=CENTER)
            my_tree.heading('Type', text='Type', anchor=CENTER)
            my_tree.heading('IMO', text='IMO', anchor=CENTER)
            my_tree.heading('Capacity', text='Capacity', anchor=CENTER)
            my_tree.heading('Condition', text='Condition', anchor=CENTER)
            my_tree.heading('Navigation Status', text='Navigation Status', anchor=CENTER)
            my_tree.heading('Embarkation', text='Embarkation', anchor=CENTER)
            my_tree.heading('Departure Time', text='Departure Time', anchor=CENTER)
            my_tree.heading('Destination', text='Destination', anchor=CENTER)
            my_tree.heading('Arrival Time', text='Arrival Time', anchor=CENTER)
            my_tree.heading('Image Location', text='Image Location', anchor=CENTER)
            my_tree.heading('BookingStatus', text='Booking Status', anchor=CENTER)


            # -------------------------------REAL DATA------------------------------
            csor.execute('select * from SHIPDATA')
            data=csor.fetchall()

            # Creating Striped Row Tags
            my_tree.tag_configure('oddrow', background='#568F8E')
            my_tree.tag_configure('evenrow', background='#386665')

            # Adding Data in our Screen
            global count
            count = 0
            for record in data:
                if count%2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', 
                                values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                                record[8], record[9], record[10], record[11]), 
                                tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', 
                                values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                                record[8], record[9], record[10], record[11]), 
                                tags=('oddrow',))
                count += 1

            # --------------Entry Boxes-----------
            # Record likha hua
            data_frame = CTkLabel(master=dataframe, text='Record')
            data_frame.pack(expand='yes', padx=13, pady = 15)

            # Name Label and Entry
            n_label = CTkLabel(data_frame, text=' Name ')
            n_label.grid(row=0, column=0, padx=10, pady=10)
            n_entry = CTkEntry(data_frame)
            n_entry.grid(row=0, column=1, padx=10, pady=10)

            # Type Label and Entry
            type_label = CTkLabel(data_frame, text='Type')
            type_label.grid(row=0, column=2, padx=10, pady=10)
            type_entry = CTkEntry(data_frame)
            type_entry.grid(row=0, column=3, padx=10, pady=10)

            # imo Label and Entry
            imo_label = CTkLabel(data_frame, text='IMO')
            imo_label.grid(row=0, column=4, padx=10, pady=10)
            imo_entry = CTkEntry(data_frame)
            imo_entry.grid(row=0, column=5, padx=10, pady=10)

            # capacity Label and Entry
            capacity_label = CTkLabel(data_frame, text='Capacity')
            capacity_label.grid(row=0, column=6, padx=10, pady=10)
            capacity_entry = CTkEntry(data_frame)
            capacity_entry.grid(row=0, column=7, padx=10, pady=10)

            # condition Label and Entry
            condition_label = CTkLabel(data_frame, text='Condition')
            condition_label.grid(row=1, column=0, padx=10, pady=10)
            condition_entry = CTkEntry(data_frame)
            condition_entry.grid(row=1, column=1, padx=10, pady=10)

            # Navigation Status Label and Entry
            navigation_status_label = CTkLabel(data_frame, text='Navigation Status')
            navigation_status_label.grid(row=1, column=2, padx=10, pady=10)
            navigation_status_entry = CTkOptionMenu(master=data_frame, values=['DOCKED', 'ON ROUTE', 'AT PORT OF CALL'])
            navigation_status_entry.grid(row=1, column=3, padx=10, pady=10)

            # Embarkation Label and Entry
            embarkation_label = CTkLabel(data_frame, text='Embarkation')
            embarkation_label.grid(row=1, column=4, padx=10, pady=10)
            embarkation_entry = CTkEntry(data_frame)
            embarkation_entry.grid(row=1, column=5, padx=10, pady=10)

            # Departure Time Label and Entry
            departure_time_label = CTkLabel(data_frame, text='Departure Time')
            departure_time_label.grid(row=1, column=6, padx=10, pady=10)

            # Use DateEntry for selecting dates
            departure_date_entry = DateEntry(data_frame, width=12, background='darkblue', foreground='white', borderwidth=2,date_pattern='yyyy-mm-dd')
            departure_date_entry.grid(row=1, column=7, padx=10, pady=10)

            # Use Combobox for selecting times
            time_values = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']

            departure_time_entry = ttk.Combobox(data_frame, values=time_values, state="readonly")
            departure_time_entry.grid(row=1, column=8, padx=8, pady=10)

            # Destination Label and Entry
            destination_label = CTkLabel(data_frame, text='Destination')
            destination_label.grid(row=2, column=0, padx=8, pady=10)
            destination_entry = CTkEntry(data_frame)
            destination_entry.grid(row=2, column=1, padx=10, pady=10)

            # Arrival Time Label and Entry
            arrival_time_label = CTkLabel(data_frame, text='Arrival Time')
            arrival_time_label.grid(row=2, column=2, padx=10, pady=10)
            
            # Use DateEntry for selecting dates
            arrival_date_entry = DateEntry(data_frame, width=12, background='darkblue', foreground='white', borderwidth=2,date_pattern='yyyy-mm-dd')
            arrival_date_entry.grid(row=2, column=3, padx=10, pady=10)
            arrival_time_entry = ttk.Combobox(data_frame, values=time_values, state="readonly")
            arrival_time_entry.grid(row=2, column=4, padx=8, pady=10)

            # Image Path Label and Entry
            image_path_label = CTkLabel(data_frame, text='Image Path')
            image_path_label.grid(row=2, column=5, padx=10, pady=10)

            image_path_entry = CTkEntry(data_frame)
            image_path_entry.grid(row=2, column=6, padx=10, pady=10)

            # Upload Image Button
            upload_button = CTkButton(master=data_frame, text='Upload Image', command=upload_image)
            upload_button.grid(row=2, column=7, padx=10, pady=10)

            # Booking Status Label and Entry
            booking_status_label = CTkLabel(data_frame, text='Booking Status')
            booking_status_label.grid(row=3, column=4, padx=10, pady=10)
            booking_status_entry = CTkOptionMenu(master=data_frame, values=['Booked', 'Not Booked'])
            booking_status_entry.grid(row=3, column=5, padx=10, pady=10)


            # --------------Functions------------------
            # Clear Entries
            def clear_entries():
                # Clearing Entry Boxes
                n_entry.delete(0, END)
                type_entry.delete(0, END)
                imo_entry.delete(0, END)
                capacity_entry.delete(0, END)
                condition_entry.delete(0, END)
                embarkation_entry.delete(0, END)
                destination_entry.delete(0, END)
                arrival_time_entry.delete(0, END)
                image_path_entry.delete(0, END)


            # Select Records
            def select_record(e):
                # Clearing Entry Boxes
                n_entry.delete(0, END)
                type_entry.delete(0, END)
                imo_entry.delete(0, END)
                capacity_entry.delete(0, END)
                condition_entry.delete(0, END)
                embarkation_entry.delete(0, END)
                destination_entry.delete(0, END)
                arrival_time_entry.delete(0, END)
                image_path_entry.delete(0, END)

                # Grabing selected record(number to be precise)
                selected = my_tree.focus()
                print(f'Selected: {selected}')
                # Grab record values
                values = my_tree.item(selected, 'values')

                # Inserting Values
                n_entry.insert(0, values[0])
                type_entry.insert(0, values[1])
                imo_entry.insert(0, values[2])
                capacity_entry.insert(0, values[3])
                condition_entry.insert(0, values[4])
                navigation_status_entry.set(values[5])
                embarkation_entry.insert(0, values[6])
                destination_entry.insert(0, values[8])
                image_path_entry.insert(0, values[10])
                booking_status_entry.set(values[11])

                if selected:
                    print("Button Show")
                    show_info.pack(side=BOTTOM,anchor=SW,padx=20,pady=15)
                else:
                    show_info.pack_forget()

            def add_record():
                global count

                count += 1

                departure_datetime_str = f"{departure_date_entry.get()} {departure_time_entry.get()}"
                arrival_datetime_str = f"{arrival_date_entry.get()} {arrival_time_entry.get()}"

                departure_datetime = datetime.strptime(departure_datetime_str, '%Y-%m-%d %H:%M')
                arrival_datetime = datetime.strptime(arrival_datetime_str, '%Y-%m-%d %H:%M')

                if arrival_datetime <= departure_datetime:
                    messagebox.showwarning('Warning!!', "Arrival Time can't be equal to or less than Departure Time!!!!!")
                    return

                if count%2==0:
                    my_tree.insert(parent='',index='end' ,iid=count, text='', values=(
                        n_entry.get(),type_entry.get(),imo_entry.get(),capacity_entry.get(),condition_entry.get(),navigation_status_entry.get(),embarkation_entry.get(),departure_datetime,destination_entry.get(),arrival_datetime, image_path_entry.get(), booking_status_entry.get()
                    ), tags=('evenrow'))
                else:
                    my_tree.insert(parent='',index='end' ,iid=count, text='', values=(
                        n_entry.get(),type_entry.get(),imo_entry.get(),capacity_entry.get(),condition_entry.get(),navigation_status_entry.get(),embarkation_entry.get(),departure_datetime,destination_entry.get(),arrival_datetime, image_path_entry.get(), booking_status_entry.get()
                    ), tags=('oddrow'))

                # Create a Ships instance for the newly added record
                new_ship = Ships(
                    name=n_entry.get(),
                    IMO_Number=imo_entry.get(),
                    capacity=capacity_entry.get(),
                    condition=condition_entry.get(),
                    navigation_status=navigation_status_entry.get(),
                    type=type_entry.get(),
                    Embarkation=embarkation_entry.get(),
                    departuretime= departure_datetime,
                    Destination=destination_entry.get(),
                    arrivaltime=arrival_datetime,
                    imagelocation=image_path_entry.get(),
                    bookingstatus = booking_status_entry.get()
                )

                new_ship.update_speed()
                
                # MySQL
                csor.execute(f"insert into SHIPDATA values('{n_entry.get()}','{type_entry.get()}',{imo_entry.get()},{capacity_entry.get()},'{condition_entry.get()}','{navigation_status_entry.get()}','{embarkation_entry.get()}','{departure_datetime}','{destination_entry.get()}','{arrival_datetime}','{image_path_entry.get()}', '{booking_status_entry.get()}')")
                db.commit()
                
                n_entry.delete(0, END)
                type_entry.delete(0, END)
                imo_entry.delete(0, END)
                capacity_entry.delete(0, END)
                condition_entry.delete(0, END)
                embarkation_entry.delete(0, END)
                destination_entry.delete(0, END)
                arrival_time_entry.delete(0, END)
                image_path_entry.delete(0, END)
                booking_status_entry.set('BOOKED')

            def update_record():
                selected = my_tree.focus()
                values = my_tree.item(selected, 'values')

                # Get date and time separately
                departure_date = departure_date_entry.get_date()
                departure_time_str = departure_time_entry.get()
                if departure_time_str:
                    departure_time = datetime.strptime(departure_time_entry.get(), '%H:%M').time()
                else:
                    departure_time=datetime.strptime(values[7], '%Y-%m-%d %H:%M:%S').time()
                departure_datetime = datetime.combine(departure_date, departure_time)

                arrival_date = arrival_date_entry.get_date()

                arrival_time_str = arrival_time_entry.get()
                # Check if arrival_time_str is not empty before parsing
                if arrival_time_str:
                    arrival_time = datetime.strptime(arrival_time_str, '%H:%M').time()
                else:
                    # Handle the case where arrival_time_str is empty, for example, set a default time
                    arrival_time = datetime.strptime(values[9], '%Y-%m-%d %H:%M:%S').time()

                # Combine the date and time
                arrival_datetime = datetime.combine(arrival_date, arrival_time)

                arrival_datetime = datetime.combine(arrival_date, arrival_time)

                if arrival_datetime <= departure_datetime:
                    messagebox.showerror("Error", "Arrival time must be greater than departure time.")
                    return 

                my_tree.item(selected, text='', values=(
                        n_entry.get(), type_entry.get(), imo_entry.get(),capacity_entry.get() ,condition_entry.get(), navigation_status_entry.get(), embarkation_entry.get(),departure_datetime ,destination_entry.get(), arrival_datetime, image_path_entry.get(), booking_status_entry.get()
                    ))
                
                # MySQL
                record_imo = my_tree.item(selected)['values'][1]
                
                csor.execute("""
                    UPDATE SHIPDATA 
                    SET Name = '{}',
                        TYPE = '{}',
                        IMO = {},
                        Capacity = {},
                        `Condition` = '{}',
                        Navigation_Status = '{}',
                        Embarkation = '{}',
                        Departure_Time = '{}',
                        Destination = '{}',
                        Arrival_Time = '{}',
                        Image = '{}',
                        BookingStatus = '{}'
                    WHERE IMO = {}
                    """.format(
                        n_entry.get(), 
                        type_entry.get(), 
                        imo_entry.get(), 
                        capacity_entry.get(),
                        condition_entry.get(), 
                        navigation_status_entry.get(), 
                        embarkation_entry.get(), 
                        departure_datetime.strftime('%Y-%m-%d %H:%M:%S'),
                        destination_entry.get(), 
                        arrival_datetime.strftime('%Y-%m-%d %H:%M:%S'),
                        image_path_entry.get(),
                        booking_status_entry.get(),
                        my_tree.item(selected)['values'][2]  # Assuming 'IMO' is at index 2
                    )
                )
                db.commit()
                
                n_entry.delete(0, END)
                type_entry.delete(0, END)
                imo_entry.delete(0, END)
                capacity_entry.delete(0, END)
                condition_entry.delete(0, END)
                embarkation_entry.delete(0, END)
                destination_entry.delete(0, END)
                arrival_time_entry.delete(0, END)
                image_path_entry.delete(0, END)
                booking_status_entry.set('Not Booked')

            # Remove One Selected
            def remove_one():
                csor.execute(f"DELETE FROM SHIPDATA WHERE IMO = {imo_entry.get()}")
                db.commit()
                x = my_tree.selection()[0]
                my_tree.delete(x)
                n_entry.delete(0, END)
                type_entry.delete(0, END)
                imo_entry.delete(0, END)
                capacity_entry.delete(0, END)
                condition_entry.delete(0, END)
                embarkation_entry.delete(0, END)
                destination_entry.delete(0, END)
                arrival_time_entry.delete(0, END)
                image_path_entry.delete(0, END)
                booking_status_entry.set('Not Booked')

            # Remove Selected
            def remove_selected():
                x = my_tree.selection()
                for record in x:
                    record_imo = my_tree.item(record)['values'][2]
                    csor.execute('DELETE FROM SHIPDATA where imo = ({})'.format(record_imo))
                    db.commit()
                    my_tree.delete(record)
                n_entry.delete(0, END)
                type_entry.delete(0, END)
                imo_entry.delete(0, END)
                capacity_entry.delete(0, END)
                condition_entry.delete(0, END)
                embarkation_entry.delete(0, END)
                destination_entry.delete(0, END)
                arrival_time_entry.delete(0, END)
                image_path_entry.delete(0, END)
                booking_status_entry.set('Not Booked')

            # Remove All Record
            def remove_all_record():
                # Remove all records from the MySQL table
                csor.execute('DELETE FROM SHIPDATA')
                db.commit()
                for record in my_tree.get_children():
                    my_tree.delete(record)
                n_entry.delete(0, END)
                type_entry.delete(0, END)
                imo_entry.delete(0, END)
                capacity_entry.delete(0, END)
                condition_entry.delete(0, END)
                embarkation_entry.delete(0, END)
                destination_entry.delete(0, END)
                arrival_time_entry.delete(0, END)
                image_path_entry.delete(0, END)
                booking_status_entry.set('Not Booked')

            # --------------Buttons----------------
            # Frame
            button_frame = CTkFrame(master=dataframe, bg_color='#2c2c2e', corner_radius=10)
            button_frame.pack(expand='no',anchor=S ,padx=15, pady=34) 

            # Update Button
            update_button = CTkButton(master=button_frame, text='Update Record',command=update_record)
            update_button.grid(row=0, column=0, padx=10, pady=10)

            add_button = CTkButton(master=button_frame, text='Add Record',command=add_record)
            add_button.grid(row=0, column=1, padx=10, pady=10)

            remove_all_button = CTkButton(master=button_frame, text='Remove All Record',command=remove_all_record)
            remove_all_button.grid(row=0, column=2, padx=10, pady=10)

            remove_one_button = CTkButton(master=button_frame, text='Remove One Selected',command=remove_one)
            remove_one_button.grid(row=0, column=3, padx=10, pady=10)

            remove_many_button = CTkButton(master=button_frame, text='Remove Many Selected',command=remove_selected)
            remove_many_button.grid(row=0, column=4, padx=10, pady=10)

            clear_entries_button = CTkButton(master=button_frame, text='Clear Entries',command=clear_entries)
            clear_entries_button.grid(row=0, column=7, padx=10, pady=10)

            # ------------Binding-----------
            my_tree.bind("<ButtonRelease-1>", select_record)

            return dataframe
        else:
            dataframe.destroy()

            return None


    mainthing('show')

    def check_and_update_navigation_status():
        global my_tree,check_and_update_navigation_status
        try:
            # Get the current time
            current_time = datetime.now()

            # Iterate through records and update navigation status if needed
            for record in my_tree.get_children():
                values = my_tree.item(record, 'values')
                arrival_time_str = values[9]  # Assuming 'Arrival Time' is at index 9

                if arrival_time_str:
                    arrival_time = datetime.strptime(arrival_time_str, '%Y-%m-%d %H:%M:%S')
                    if current_time >= arrival_time:
                        # Update navigation status to 'Docked'
                        csor.execute("""
                            UPDATE SHIPDATA 
                            SET Navigation_Status = 'DOCKED'
                            WHERE IMO = {}
                        """.format(values[2]))  # Assuming 'IMO' is at index 2
                        db.commit()

                        # Update the Treeview
                        my_tree.item(record, values=(values[0], values[1], values[2], values[3], values[4], 'DOCKED', values[6], values[7], values[8], values[9], values[10], values[11]))
            for i in range(0,20):
                # Schedule the function to run again after 60 seconds
                root.after(10000,check_and_update_navigation_status)

        except Exception as e:
            print(f"Error in background thread: {e}")

    # Start the background thread
    check_and_update_navigation_status()

    def  display_ship_details(ship_name,ship_type,imo_number,capacity,condition,navigation_status,embarkation,departuretime,destination,arrivaltime,imagepath,bookingstatus):
        global detail_frame
        detail_frame = Frame(root, width=1200, height=600, bg='#161f1e')
        detail_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Display ship details
        toplabel = CTkLabel(master=detail_frame)
        toplabel.grid(row=0, column=0, padx=13, pady=15)

        ship_name_label = CTkLabel(toplabel, text=f"Name: {ship_name}", bg_color='#161f1e', fg_color='#4d81c9', font=("Helvetica", 20), corner_radius=5)
        ship_name_label.grid(row=1, column=0, pady=10, padx=20)

        imageframe = CTkFrame(toplabel, width=width//2, height=height//2)
        imageframe.grid(row=0, column=0)

        background_img = Image.open(imagepath)
        background_img = background_img.resize((500, 500))
        background_tkimg = ImageTk.PhotoImage(background_img)

        imagelabel = CTkLabel(imageframe,text='' ,image=background_tkimg)
        imagelabel.grid(row=0, column=1)

        otherdetaillabel = CTkLabel(master=detail_frame)
        otherdetaillabel.grid(row=1, column=0, padx=13, pady=15)

        ship_type_label = CTkLabel(otherdetaillabel, text=f"Type: {ship_type}", bg_color='#161f1e',fg_color='#4d81c9', corner_radius=5)
        ship_type_label.grid(row=0, column=0, pady=10, padx=13)

        imo_label = CTkLabel(otherdetaillabel, text=f"IMO: {imo_number}", bg_color='#161f1e', fg_color='#4d81c9', font=("Helvetica", 14), corner_radius=5)
        imo_label.grid(row=0, column=1, pady=10, padx=13)

        capacity_label = CTkLabel(otherdetaillabel, text=f"Capacity: {capacity}", bg_color='#161f1e', fg_color='#4d81c9', font=("Helvetica", 14), corner_radius=5)
        capacity_label.grid(row=0, column=2, pady=10, padx=13)

        condition_label = CTkLabel(otherdetaillabel, text=f"Condition: {condition}", bg_color='#161f1e', fg_color='#4d81c9', font=("Helvetica", 14), corner_radius=5)
        condition_label.grid(row=1, column=0, pady=10, padx=13)

        navigation_status_label = CTkLabel(otherdetaillabel, text=f"Navigation Status: {navigation_status}", bg_color='#161f1e', fg_color='#4d81c9', font=("Helvetica", 14), corner_radius=5)
        navigation_status_label.grid(row=1, column=1, pady=10, padx=13)

        embarkation_label = CTkLabel(otherdetaillabel, text=f"Embarkation: {embarkation}", bg_color='#161f1e', fg_color='#4d81c9', font=("Helvetica", 14), corner_radius=5)
        embarkation_label.grid(row=1, column=2, pady=10, padx=13)

        departure_time_label = CTkLabel(otherdetaillabel, text=f"Departure Time: {departuretime}", bg_color='#161f1e', fg_color='#4d81c9', font=("Helvetica", 14), corner_radius=5)
        departure_time_label.grid(row=1, column=2, pady=10, padx=13)

        destination_label = CTkLabel(otherdetaillabel, text=f"Destination: {destination}", bg_color='#161f1e', fg_color='#4d81c9', font=("Helvetica", 14), corner_radius=5)
        destination_label.grid(row=2, column=0, pady=10, padx=13)

        arrival_time_label = CTkLabel(otherdetaillabel, text=f"Arrival Time: {arrivaltime}", bg_color='#161f1e', fg_color='#4d81c9', font=("Helvetica", 14), corner_radius=5)
        arrival_time_label.grid(row=2, column=0, pady=10, padx=13)

    def ship_info_detail():
        global dataframe,detail_frame,back_button,logoutbtn
        # Button to go back to the main view
        backbtn_img = PhotoImage(file = r"E:\Project CS\Vessel Traffic Management System\GUI\photos\backbtn.png")
        # Resize the image to, for example, 25% of its original size
        backbtn_img = backbtn_img.subsample(5, 5)
        back_button = CTkButton(frame1,text='',image=backbtn_img, command=backbtn)
        back_button.pack(side=TOP, anchor='nw', pady=20, padx=20)

        selected = my_tree.focus()
        print('final')
        values = my_tree.item(selected, 'values')
        print(f'Selected Ship: {selected}')
        if dataframe:
            dataframe.destroy()
            show_info.pack_forget()
            logoutbtn.pack_forget()
            print('hello2')
        if selected:
            x = list(values)
            # Iterate up to the second-to-last element
            i = 0
            while i < len(x) - 1:
                # Check if the next element is equal to the current one
                if x[i + 1] == x[i]:
                    # If yes, remove the duplicate element
                    x.pop(i + 1)
                else:
                    # If no, move to the next element
                    i += 1
            display_ship_details(*x)
            print('nothing')
        
    def backbtn():
        print('hello')
        global detail_frame,back_button,logoutbtn
        detail_frame.destroy()
        back_button.destroy()
        logoutbtn.pack(side=TOP, anchor=NW, padx=10, pady=5)
        mainthing('show')

    # Button To see data
    btn_img = Image.open(r"E:\Project CS\Vessel Traffic Management System\GUI\photos\search.png")
    btn_img = btn_img.resize((50,50))
    btn_tkimg = ImageTk.PhotoImage(btn_img)
    show_info = CTkButton(master=frame1,text='',image=btn_tkimg,command=ship_info_detail,cursor='hand2',width=50,height=50)
signin_window()
# Schedule the function to run again after 60 seconds
# End
root.mainloop()