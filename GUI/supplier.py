from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from datetime import *
import time,random
import mysql.connector as mysql
from customtkinter import *

# -----------------------------------------------------------------------------
# ----------------------------------GUI----------------------------------------
# -----------------------------------------------------------------------------
root = Tk()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width,height))
root.configure(bg='#ffffff')

# At the beginning of your script
ship_image_tk_list = []



class Ships:
    speed = 0
    # IMO Number = The International Maritime Organization (IMO) number uniquely identifies each seagoing ship. It is an important reference for tracking and managing vessels.
    def __init__(self,name,IMO_Number,condition,capacity,navigation_status,type,bookingstatus,Embarkation,departuretime,Destination,arrivaltime, imagelocation):
        self.Name = name
        self.Condition = condition
        self.Navigation_Status = navigation_status
        self.IMO_Number = IMO_Number
        self.Type = type
        self.Embarkation = Embarkation
        self.BookingStatus=bookingstatus
        self.Departure_Time = departuretime
        self.Destination = Destination
        self.Arrival_Time = arrivaltime
        self.Image_Location = imagelocation
        self.Capacity = capacity

    @classmethod
    def change_condition(cls, condition):
        cls.condition = condition
    
    @classmethod
    def change_navigation_status(cls, navigation_status):
        cls.navigation_status = navigation_status

    def update_speed(self):
        self.speed = random.randint(25, 30)
# -----------------------------------------------------------------------------
# --------------------------------Functions------------------------------------
# -----------------------------------------------------------------------------
# Connecting Database
def connect_to_database():
    db = mysql.connect(host="localhost", user="root", password="nakuldesai2510",database="vtms")

    return db

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
        Label(card_frame, text=f"Ship: {ship_data.Name}", width=60).grid(row=1, column=0, sticky="w")
        Label(card_frame, text=f"Embarkation: {ship_data.Embarkation}", width=60).grid(row=2, column=0, sticky="w")

        # Display booking status
        if ship_data.BookingStatus == "BOOKED":
            Label(card_frame, text="Booking Status: BOOKED", fg="green", width=60).grid(row=3, column=0, columnspan=2, pady=5)
        else:
            Label(card_frame, text="Booking Status: NOT BOOKED", fg="red", width=60).grid(row=3, column=0, columnspan=2, pady=5)
    
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
    for i in ships_data:
        print(i)
        print()

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
sidebar = Frame(root,bg='#ffffff',height=height,width=(width//5)-15)
sidebar.pack(side=LEFT)
sidebar.pack_propagate(False)

# ---------------------------------Header--------------------------------------
# ---------------------------------------------------------------Main Frame---------------------------------------------------------------
main_frame = Frame(root, highlightbackground='black', highlightthickness=2, width=width, height=height)
main_frame.pack(side=LEFT)
main_frame.pack_propagate(False)

header = Frame(main_frame, bg='#009df4', width=width, height=(height//10)-10)
header.pack()

logout = Button(header, text='Logout', bg='#32cf8e', font=('', 13, 'bold'), bd=0, fg='white', 
                cursor='hand2', activebackground='#32cf8e')
logout.place(x=1080, y=30)

# ------------------------------------------------------------------------------------
# -------User--------
user_pic = Image.open(r"photos\user.png")
user_pic = user_pic.resize((width//10,height//5))
user_tkimg = ImageTk.PhotoImage(user_pic)

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
show_time()

# --------------------End-------------------


if __name__ == '__main__':
    indicate(view_ships_indicator, view_ship)
    root.mainloop()