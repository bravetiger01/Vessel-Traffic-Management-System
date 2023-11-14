from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image, ImageDraw, ImageFont
import random
import mysql.connector as connector
from customtkinter import *
from tkcalendar import DateEntry
from datetime import datetime, timedelta
import threading


# -----------------------------------------------Ships-------------------------------------------------
class Ships:
    speed = 0
    # IMO Number = The International Maritime Organization (IMO) number uniquely identifies each seagoing ship. It is an important reference for tracking and managing vessels.
    def __init__(self, name, IMO_Number , condition, capacity, navigation_status, type, Embarkation,departuretime,Destination,arrivaltime, imagelocation):
        self.Name = name
        self.Condition = condition
        self.Navigation_Status = navigation_status
        self.IMO_Number = IMO_Number
        self.Type = type
        self.Embarkation = Embarkation
        self.Departure_Time = arrivaltime
        self.Destination = Destination
        self.Arrival_Time = departuretime
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



# ------------------------------------------GUI-------------------------------------------
root = Tk()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width,height))

frame1 = CTkFrame(master=root, width=width, height=height)
frame1.pack(fill=BOTH, expand=True)

# bglabel = Label(frame1, image=background_tkimg)
# bglabel.place(x=0, y=0)

mydata = connector.connect(host='localhost', user='root', password='nakuldesai2510', database='vtms')
csor = mydata.cursor()


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
    global dataframe, my_tree, image_path_entry, my_tree
    if x == 'show':
        dataframe = CTkFrame(master=frame1, width=500, height=1000,
                        corner_radius=15, border_width=0)

        dataframe.place(relx=0.5, rely=0.5, anchor=CENTER)
        dataframe.pack_configure(expand=True, padx=10)
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
        my_tree['columns'] = ('Name','Type','IMO','Capacity','Condition','Navigation Status','Embarkation','Departure Time','Destination','Arrival Time','Image Location')

        # Formating Columns
        my_tree.column('#0', width=0, stretch=NO)
        my_tree.column('Name', anchor=CENTER, width=150)
        my_tree.column('Type', anchor=CENTER, width=150)
        my_tree.column('IMO', anchor=CENTER, width=110)
        my_tree.column('Capacity', anchor=CENTER, width=110)
        my_tree.column('Condition', anchor=CENTER, width=150)
        my_tree.column('Navigation Status', anchor=CENTER, width=150)
        my_tree.column('Embarkation', anchor=CENTER, width=100)
        my_tree.column('Departure Time', anchor=CENTER, width=100)
        my_tree.column('Destination', anchor=CENTER, width=150)
        my_tree.column('Arrival Time', anchor=CENTER, width=100)
        my_tree.column('Image Location', anchor=CENTER, width=90)


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
                            record[8], record[9], record[10]), 
                            tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', 
                            values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                            record[8], record[9], record[10]), 
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
        departure_date_entry = DateEntry(data_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
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
        arrival_date_entry = DateEntry(data_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
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
            # Grab record values
            values = my_tree.item(selected, 'values')

            # Inserting Values
            n_entry.insert(0, values[0])
            type_entry.insert(0, values[1])
            imo_entry.insert(0, values[2])
            capacity_entry.insert(0, values[3])
            condition_entry.insert(0, values[4])
            embarkation_entry.insert(0, values[6])
            destination_entry.insert(0, values[8])
            image_path_entry.insert(0, values[10])

            if selected:
                show_info.pack(side=BOTTOM, anchor=SW, padx=10, pady=40)
            else:
                show_info.pack_forget()

        def add_record():
            global count

            count += 1

            departure_datetime_str = f"{departure_date_entry.get()} {departure_time_entry.get()}"
            arrival_datetime_str = f"{arrival_date_entry.get()} {arrival_time_entry.get()}"

            departure_datetime = datetime.strptime(departure_datetime_str, '%Y-%m-%d %H:%M')
            arrival_datetime = datetime.strptime(arrival_datetime_str, '%Y-%m-%d %H:%M')

            if count%2==0:
                my_tree.insert(parent='',index='end' ,iid=count, text='', values=(
                    n_entry.get(),type_entry.get(),imo_entry.get(),capacity_entry.get(),condition_entry.get(),navigation_status_entry.get(),embarkation_entry.get(),departure_datetime,destination_entry.get(),arrival_datetime, image_path_entry.get()
                ), tags=('evenrow'))
            else:
                my_tree.insert(parent='',index='end' ,iid=count, text='', values=(
                    n_entry.get(),type_entry.get(),imo_entry.get(),capacity_entry.get(),condition_entry.get(),navigation_status_entry.get(),embarkation_entry.get(),departure_datetime,destination_entry.get(),arrival_datetime, image_path_entry.get()
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
                imagelocation=image_path_entry.get()
            )

            new_ship.update_speed()
            
            # MySQL
            csor.execute("insert into SHIPDATA values('{}','{}',{},{},'{}','{}','{}','{}','{}','{}','{}')".
                        format(n_entry.get(),type_entry.get(),imo_entry.get(),capacity_entry.get(),condition_entry.get(),navigation_status_entry.get(),embarkation_entry.get(),departure_datetime,destination_entry.get(),arrival_datetime,image_path_entry.get()))
            mydata.commit()
            
            n_entry.delete(0, END)
            type_entry.delete(0, END)
            imo_entry.delete(0, END)
            capacity_entry.delete(0, END)
            condition_entry.delete(0, END)
            embarkation_entry.delete(0, END)
            
            
            destination_entry.delete(0, END)
            arrival_time_entry.delete(0, END)
            image_path_entry.delete(0, END)

        def update_record():
            selected = my_tree.focus()

            # Get date and time separately
            departure_date = departure_date_entry.get_date()
            departure_time = departure_time_entry.get()

            departure_datetime = datetime.combine(departure_date, departure_time)

            arrival_date = arrival_date_entry.get_date()
            arrival_time = arrival_time_entry.get()

            arrival_datetime = datetime.combine(arrival_date, arrival_time)

            my_tree.item(selected, text='', values=(
                    n_entry.get(), type_entry.get(), imo_entry.get(),capacity_entry.get() ,condition_entry.get(), navigation_status_entry.get(), embarkation_entry.get(),departure_datetime ,destination_entry.get(), arrival_datetime
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
                    Departure = '{}',
                    Arrival_Time = '{}',
                    Image = '{}'
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
                    my_tree.item(selected)['values'][2]  # Assuming 'IMO' is at index 2
                )
            )
            mydata.commit()
            
            n_entry.delete(0, END)
            type_entry.delete(0, END)
            imo_entry.delete(0, END)
            capacity_entry.delete(0, END)
            condition_entry.delete(0, END)
            embarkation_entry.delete(0, END)
            
            
            destination_entry.delete(0, END)
            arrival_time_entry.delete(0, END)
            

        # Remove One Selected
        def remove_one():

            csor.execute(f"DELETE FROM SHIPDATA WHERE IMO = {imo_entry.get()}")
            mydata.commit()

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

        # Remove Selected
        def remove_selected():
            x = my_tree.selection()
            for record in x:
                record_imo = my_tree.item(record)['values'][2]
                csor.execute('DELETE FROM SHIPDATA where imo = ({})'.format(record_imo))
                mydata.commit()
                my_tree.delete(record)
            n_entry.delete(0, END)
            type_entry.delete(0, END)
            imo_entry.delete(0, END)
            capacity_entry.delete(0, END)
            condition_entry.delete(0, END)
            embarkation_entry.delete(0, END)
            
            
            destination_entry.delete(0, END)
            arrival_time_entry.delete(0, END)

        # Remove All Record
        def remove_all_record():
            # Remove all records from the MySQL table
            csor.execute('DELETE FROM SHIPDATA')
            mydata.commit()
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

        # background_thread = threading.Thread(target=check_and_update_navigation_status, daemon=True)
        # background_thread.start()

        return dataframe
    else:
        dataframe.destroy()

        return None


mainthing('show')

def check_and_update_navigation_status():
    global my_tree
    try:
        # Get the current time
        current_time = datetime.now()

        # Iterate through records and update navigation status if needed
        for record in my_tree.get_children():
            values = my_tree.item(record, 'values')
            x = list(values)
            for i in range (0,len(x)):
                if x[i] == x[i-1]:
                    x.remove(i)
                print(x)
            arrival_time_str = x[9]  # Assuming 'Arrival Time' is at index 9

            if arrival_time_str:
                arrival_time = datetime.strptime(arrival_time_str, '%Y-%m-%d %H:%M:%S')
                if current_time >= arrival_time:
                    # Update navigation status to 'Docked'
                    csor.execute("""
                        UPDATE SHIPDATA 
                        SET Navigation_Status = 'DOCKED'
                        WHERE IMO = {}
                    """.format(values[2]))  # Assuming 'IMO' is at index 2
                    mydata.commit()

                    # Update the Treeview
                    my_tree.item(record, values=(values[0], values[1], values[2], values[3], values[4], values[5], 'DOCKED', values[6], values[7], values[8], values[9], values[10]))

        # Schedule the function to run again after 60 seconds
        root.after(60000, check_and_update_navigation_status)

    except Exception as e:
        print(f"Error in background thread: {e}")

# Start the background thread
check_and_update_navigation_status()

def   display_ship_details(ship_name,ship_type,imo_number,capacity,condition,navigation_status,embarkation,arrivaltime,destination,destinationtime,imagepath):
    global detail_frame
    detail_frame = Frame(root, width=1200, height=600, bg='#161f1e')
    detail_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Display ship details
    toplabel = CTkLabel(master=detail_frame)
    toplabel.grid(row=0, column=0, padx=13, pady=15)

    ship_name_label = CTkLabel(toplabel, text=f"Name: {ship_name}", bg_color='#161f1e', fg_color='#4d81c9', font=("Helvetica", 20))
    ship_name_label.grid(row=1, column=0, pady=10, padx=20)

    imageframe = CTkFrame(toplabel, width=width//2, height=height//2)
    imageframe.grid(row=0, column=0)

    background_img = Image.open(imagepath)
    background_img = background_img.resize((500, 500))
    background_tkimg = ImageTk.PhotoImage(background_img)

    imagelabel = CTkLabel(imageframe, image=background_tkimg)
    imagelabel.grid(row=0, column=1, padx=20, pady=20)

    otherdetaillabel = CTkLabel(master=detail_frame)
    otherdetaillabel.grid(row=1, column=0, padx=13, pady=15)

    ship_type_label = CTkLabel(otherdetaillabel, text=f"Type: {ship_type}", bg_color='#161f1e',fg_color='#4d81c9')
    ship_type_label.grid(row=0, column=0, pady=10, padx=13)

    imo_label = CTkLabel(otherdetaillabel, text=f"IMO: {imo_number}", bg_color='#161f1e', fg_color='#4d81c9', font=("Helvetica", 14))
    imo_label.grid(row=0, column=1, pady=10, padx=13)

    capacity_label = CTkLabel(otherdetaillabel, text=f"Capacity: {capacity}", bg_color='#161f1e', fg_color='#4d81c9', font=("Helvetica", 14))
    capacity_label.grid(row=0, column=2, pady=10, padx=13)

    condition_label = CTkLabel(otherdetaillabel, text=f"Condition: {condition}", bg_color='#161f1e', fg_color='#4d81c9', font=("Helvetica", 14))
    condition_label.grid(row=1, column=0, pady=10, padx=13)

    navigation_status_label = CTkLabel(otherdetaillabel, text=f"Navigation Status: {navigation_status}", bg_color='#161f1e', fg_color='#4d81c9', font=("Helvetica", 14))
    navigation_status_label.grid(row=1, column=1, pady=10, padx=13)

    embarkation_label = CTkLabel(otherdetaillabel, text=f"Embarkation: {embarkation}", bg_color='#161f1e', fg_color='#4d81c9', font=("Helvetica", 14))
    embarkation_label.grid(row=1, column=2, pady=10, padx=13)

    destination_label = CTkLabel(otherdetaillabel, text=f"Destination: {destination}", bg_color='#161f1e', fg_color='#4d81c9', font=("Helvetica", 14))
    destination_label.grid(row=2, column=0, pady=10, padx=13)


def ship_info_detail():
    global dataframe, detail_frame, back_button
    


    # Button to go back to the main view
    backbtn_img = PhotoImage(file = r"E:\Project CS\Vessel Traffic Management System\photos\backbtn.png")
    # Resize the image to, for example, 25% of its original size
    backbtn_img = backbtn_img.subsample(5, 5)
    back_button = CTkButton(frame1,text='',image=backbtn_img, command=backbtn)
    back_button.pack(side=TOP, anchor='nw', pady=20, padx=20)

    selectedship = my_tree.focus()
    if selectedship:
        values = my_tree.item(selectedship, 'values')
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
        print(x)
        display_ship_details(*x)
    if dataframe:
        dataframe.destroy()
        show_info.pack_forget()
    
    
def backbtn():
    print('hello')
    global detail_frame, back_button
    detail_frame.destroy()
    back_button.destroy()
    mainthing('show')


# Button To see data
btn_img = PhotoImage(file = r"E:\Project CS\Vessel Traffic Management System\photos\search.png")
show_info = CTkButton(master=frame1,text='',image=btn_img, command=ship_info_detail, bg_color="transparent",cursor='hand2', width=23)
# --------------------End-------------------
root.mainloop()