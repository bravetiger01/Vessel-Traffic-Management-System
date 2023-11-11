from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image, ImageDraw, ImageFont
import random
import mysql.connector as connector


# -----------------------------------------------Ships-------------------------------------------------
class Ships:
    speed = 0
    # IMO Number = The International Maritime Organization (IMO) number uniquely identifies each seagoing ship. It is an important reference for tracking and managing vessels.
    def __init__(self, name, IMO_Number , condition, capacity, navigation_status, type, Embarkation, Destination):
        self.Name = name
        self.Condition = condition
        self.Navigation_Status = navigation_status
        self.IMO_Number = IMO_Number
        self.Type = type
        self.Embarkation = Embarkation
        self.Destination = Destination
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
root.resizable(False,False)
root.configure(bg='white')

frame1 = Frame(root, width=width, height=height)
frame1.pack(fill=BOTH, expand=True)


background_img = Image.open(r"E:\Project CS\Vessel Traffic Management System\GUI\photos\loginphoto.jpg")
background_img = background_img.resize((root.winfo_screenwidth(),root.winfo_screenheight()))
background_tkimg = ImageTk.PhotoImage(background_img)

bglabel = Label(frame1, image=background_tkimg)
bglabel.place(x=0, y=0)

mydata = connector.connect(host='localhost', user='root', password='nakuldesai2510', database='vtms')
csor = mydata.cursor()




# ---------------------------------------------Data Showing-------------------------------------------
frame = Frame(frame1, width=500, height=1000)
frame.pack(expand=True)

frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Button To see data
btn_img = PhotoImage(file = r"E:\Project CS\Vessel Traffic Management System\photos\search.png")

def ship_info_detail():
    frame1.destroy()

    frame2 = Frame(root, width= width, height= height)
    frame2.pack(expand=True, fill=BOTH)

    bglabel = Label(frame2, image=background_tkimg)
    bglabel.place(x=0, y=0)

    




show_info = Button(frame1, image=btn_img, command=ship_info_detail, borderwidth=0, bd=0)
show_info.pack(side=BOTTOM, anchor=SW, padx=10, pady=40)


# -----------------------------Treeview------------------------------------
# Style
style = ttk.Style()

# Theme
style.theme_use('default')

# Treeiew colors
style.configure('Treeview',
                background='#D3D3D3',
                forground ='black',
                rowheight = 25,
                fiedbackground='#D3D3D3')

# Changing selescted entry colour
style.map('Treeview',
          background=[('selected', '#347083')])

# Treeview Frame
tree_frame = Frame(frame)
tree_frame.pack(pady=10)

# Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# --------------Treeview--------------
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended')
my_tree.pack()

# Configuring Scrollbar
tree_scroll.config(command=my_tree.yview)

# Defining Columns
my_tree['columns'] = ('Name', 'Type', 'IMO','Capacity','Condition' ,'Navigation Status', 'Embarkation', 'Destination')

# Formating Columns
my_tree.column('#0', width=0, stretch=NO)
my_tree.column('Name', anchor=CENTER, width=140)
my_tree.column('Type', anchor=CENTER, width=140)
my_tree.column('IMO', anchor=CENTER, width=100)
my_tree.column('Capacity', anchor=CENTER, width=100)
my_tree.column('Condition', anchor=CENTER, width=140)
my_tree.column('Navigation Status', anchor=CENTER, width=140)
my_tree.column('Embarkation', anchor=CENTER, width=140)
my_tree.column('Destination', anchor=CENTER, width=140)


# Creating Heading
my_tree.heading('#0', text='', anchor=W)
my_tree.heading('Name', text='Name', anchor=CENTER)
my_tree.heading('Type', text='Type', anchor=CENTER)
my_tree.heading('IMO', text='IMO', anchor=CENTER)
my_tree.heading('Capacity', text='Capacity', anchor=CENTER)
my_tree.heading('Condition', text='Condition', anchor=CENTER)
my_tree.heading('Navigation Status', text='Navigation Status', anchor=CENTER)
my_tree.heading('Embarkation', text='Embarkation', anchor=CENTER)
my_tree.heading('Destination', text='Destination', anchor=CENTER)


# -------------------------------REAL DATA------------------------------
csor.execute('select * from SHIPDATA')
data=csor.fetchall()

# Creating Striped Row Tags
my_tree.tag_configure('oddrow', background='white')
my_tree.tag_configure('evenrow', background='lightblue')

# Adding Data in our Screen
global count
count = 0
for record in data:
    if count%2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text='', 
                       values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), 
                       tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text='', 
                       values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), 
                       tags=('oddrow',))
    count += 1

# --------------Entry Boxes-----------
# Record likha hua
data_frame = LabelFrame(frame, text='Record')
data_frame.pack(fill='x', expand='yes', padx=20)

# Name Label and Entry
n_label = Label(data_frame, text='Name')
n_label.grid(row=0, column=0, padx=10, pady=10)
n_entry = Entry(data_frame)
n_entry.grid(row=0, column=1, padx=10, pady=10)

# Type Label and Entry
type_label = Label(data_frame, text='Type')
type_label.grid(row=0, column=2, padx=10, pady=10)
type_entry = Entry(data_frame)
type_entry.grid(row=0, column=3, padx=10, pady=10)

# imo Label and Entry
imo_label = Label(data_frame, text='IMO')
imo_label.grid(row=0, column=4, padx=10, pady=10)
imo_entry = Entry(data_frame)
imo_entry.grid(row=0, column=5, padx=10, pady=10)

# imo Label and Entry
capacity_label = Label(data_frame, text='Capacity')
capacity_label.grid(row=0, column=4, padx=10, pady=10)
capacity_entry = Entry(data_frame)
capacity_entry.grid(row=0, column=5, padx=10, pady=10)

# condition Label and Entry
condition_label = Label(data_frame, text='Condition')
condition_label.grid(row=1, column=0, padx=10, pady=10)
condition_entry = Entry(data_frame)
condition_entry.grid(row=1, column=1, padx=10, pady=10)

# Navigation Status Label and Entry
navigation_status_label = Label(data_frame, text='Navigation Status')
navigation_status_label.grid(row=1, column=2, padx=10, pady=10)
navigation_status_entry = Entry(data_frame)
navigation_status_entry.grid(row=1, column=3, padx=10, pady=10)

# Embarkation Label and Entry
embarkation_label = Label(data_frame, text='Embarkation')
embarkation_label.grid(row=1, column=4, padx=10, pady=10)
embarkation_entry = Entry(data_frame)
embarkation_entry.grid(row=1, column=5, padx=10, pady=10)

# Destination Label and Entry
destination_label = Label(data_frame, text='Destination')
destination_label.grid(row=1, column=6, padx=10, pady=10)
destination_entry = Entry(data_frame)
destination_entry.grid(row=1, column=7, padx=10, pady=10)

# --------------Functions------------------
# Clear Entries
def clear_entries():
    # Clearing Entry Boxes
    n_entry.delete(0, END)
    type_entry.delete(0, END)
    imo_entry.delete(0, END)
    capacity_entry.delete(0, END)
    condition_entry.delete(0, END)
    navigation_status_entry.delete(0, END)
    embarkation_entry.delete(0, END)
    destination_entry.delete(0, END)


# Select Records
def select_record(e):
    # Clearing Entry Boxes
    n_entry.delete(0, END)
    type_entry.delete(0, END)
    imo_entry.delete(0, END)
    capacity_entry.delete(0, END)
    condition_entry.delete(0, END)
    navigation_status_entry.delete(0, END)
    embarkation_entry.delete(0, END)
    destination_entry.delete(0, END)

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
    navigation_status_entry.insert(0, values[5])
    embarkation_entry.insert(0, values[6])
    destination_entry.insert(0, values[7])

def add_record():
    global count

    count += 1

    if count%2==0:
        my_tree.insert(parent='',index='end' ,iid=count, text='', values=(
            n_entry.get(), type_entry.get(), imo_entry.get(),capacity_entry.get() ,condition_entry.get(), navigation_status_entry.get(), embarkation_entry.get(), destination_entry.get()
        ), tags=('evenrow'))
    else:
        my_tree.insert(parent='',index='end' ,iid=count, text='', values=(
            n_entry.get(), type_entry.get(), imo_entry.get(),capacity_entry.get() ,condition_entry.get(), navigation_status_entry.get(), embarkation_entry.get(), destination_entry.get()
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
        Destination=destination_entry.get()
    )

    new_ship.update_speed()
    
    # MySQL
    csor.execute("insert into SHIPDATA values('{}', '{}', {}, '{}', '{}', '{}', '{}')".
                 format(n_entry.get(), type_entry.get(), imo_entry.get(),capacity_entry.get() ,condition_entry.get(), navigation_status_entry.get(), embarkation_entry.get(), destination_entry.get()))
    mydata.commit()
    
    n_entry.delete(0, END)
    type_entry.delete(0, END)
    imo_entry.delete(0, END)
    capacity_entry.delete(0, END)
    condition_entry.delete(0, END)
    navigation_status_entry.delete(0, END)
    embarkation_entry.delete(0, END)
    destination_entry.delete(0, END)

def update_record():
    selected = my_tree.focus()

    my_tree.item(selected, text='', values=(
            n_entry.get(), type_entry.get(), imo_entry.get(),capacity_entry.get() ,condition_entry.get(), navigation_status_entry.get(), embarkation_entry.get(), destination_entry.get()
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
            Departure = '{}' 
        WHERE IMO = {}
        """.format(
            n_entry.get(), 
            type_entry.get(), 
            imo_entry.get(), 
            capacity_entry.get(),
            condition_entry.get(), 
            navigation_status_entry.get(), 
            embarkation_entry.get(), 
            destination_entry.get(), 
            my_tree.item(selected)['values'][2]  # Assuming 'IMO' is at index 2
        )
    )
    mydata.commit()
    
    n_entry.delete(0, END)
    type_entry.delete(0, END)
    imo_entry.delete(0, END)
    capacity_entry.delete(0, END)
    condition_entry.delete(0, END)
    navigation_status_entry.delete(0, END)
    embarkation_entry.delete(0, END)
    destination_entry.delete(0, END)
    

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
    navigation_status_entry.delete(0, END)
    embarkation_entry.delete(0, END)
    destination_entry.delete(0, END)

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
    navigation_status_entry.delete(0, END)
    embarkation_entry.delete(0, END)
    destination_entry.delete(0, END)

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
    navigation_status_entry.delete(0, END)
    embarkation_entry.delete(0, END)
    destination_entry.delete(0, END)

# Move Up
def up():
    messagebox.showinfo('Sorry!', 'This function is not available right now')
    # rows = my_tree.selection()
    # for row in rows:
    #     my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)
# Move Down
def down():
    messagebox.showinfo('Sorry!', 'This function is not available right now')
    # rows = my_tree.selection()
    # for row in reversed(rows):
    #     my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)


# --------------Buttons----------------
# Frame
button_frame = LabelFrame(frame, text='Commands')
button_frame.pack(fill='x', expand='yes', padx=20) 

# Update Button
update_button = Button(button_frame, text='Update Record', command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text='Add Record', command=add_record)
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = Button(button_frame, text='Remove All Record', command=remove_all_record)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text='Remove One Selected', command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text='Remove Many Selected', command=remove_selected)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(button_frame, text='Move Up', command=up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text='Move Down', command=down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

clear_entries_button = Button(button_frame, text='Clear Entries', command=clear_entries)
clear_entries_button.grid(row=0, column=7, padx=10, pady=10)

# ------------Binding-----------
my_tree.bind("<ButtonRelease-1>", select_record)

# --------------------End-------------------
root.mainloop()