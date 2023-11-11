from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import mysql.connector as connector

# ---------------------GUI-------------------
root = Tk()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width,height))
root.resizable(False,False)
root.configure(bg='white')

background_img = Image.open(r"E:\Project CS\Vessel Traffic Management System\GUI\photos\loginphoto.jpg")
background_img = background_img.resize((root.winfo_screenwidth(),root.winfo_screenheight()))
background_tkimg = ImageTk.PhotoImage(background_img)

bglabel = Label(root, image=background_tkimg)
bglabel.place(x=0, y=0)

mydata = connector.connect(host='localhost', user='root', password='nakuldesai2510', database='CRM_tool')
csor = mydata.cursor()


# ---------------------------------------------Data Showing-------------------------------------------
frame = Frame(root, width=500, height=1000)
frame.pack(expand=True)

frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# -----------------------------------------Treeview------------------------------------
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
my_tree['columns'] = ('First Name', 'Last Name', 'ID', 'Address', 'City', 'State', 'Zipcode')

# Formating Columns
my_tree.column('#0', width=0, stretch=NO)
my_tree.column('First Name', anchor=CENTER, width=140)
my_tree.column('Last Name', anchor=CENTER, width=140)
my_tree.column('ID', anchor=CENTER, width=100)
my_tree.column('Address', anchor=CENTER, width=140)
my_tree.column('City', anchor=CENTER, width=140)
my_tree.column('State', anchor=CENTER, width=140)
my_tree.column('Zipcode', anchor=CENTER, width=140)


# Creating Heading
my_tree.heading('#0', text='', anchor=W)
my_tree.heading('First Name', text='First Name', anchor=CENTER)
my_tree.heading('Last Name', text='Last Name', anchor=CENTER)
my_tree.heading('ID', text='ID', anchor=CENTER)
my_tree.heading('Address', text='Address', anchor=CENTER)
my_tree.heading('City', text='City', anchor=CENTER)
my_tree.heading('State', text='State', anchor=CENTER)
my_tree.heading('Zipcode', text='Zipcode', anchor=CENTER)


# ------------------------------------Fake Data---------------------------------------
# data = [
# 	["John", "Elder", 1, "123 Elder St.", "Las Vegas", "NV", "89137"],
# 	["Mary", "Smith", 2, "435 West Lookout", "Chicago", "IL", "60610"],
# 	["Tim", "Tanaka", 3, "246 Main St.", "New York", "NY", "12345"],
# 	["Erin", "Erinton", 4, "333 Top Way.", "Los Angeles", "CA", "90210"],
# 	["Bob", "Bobberly", 5, "876 Left St.", "Memphis", "TN", "34321"],
# 	["Steve", "Smith", 6, "1234 Main St.", "Miami", "FL", "12321"],
# 	["Tina", "Browne", 7, "654 Street Ave.", "Chicago", "IL", "60611"],
# 	["Mark", "Lane", 8, "12 East St.", "Nashville", "TN", "54345"],
# 	["John", "Smith", 9, "678 North Ave.", "St. Louis", "MO", "67821"],
# 	["Mary", "Todd", 10, "9 Elder Way.", "Dallas", "TX", "88948"],
# 	["John", "Lincoln", 11, "123 Elder St.", "Las Vegas", "NV", "89137"],
# 	["Mary", "Bush", 12, "435 West Lookout", "Chicago", "IL", "60610"],
# 	["Tim", "Reagan", 13, "246 Main St.", "New York", "NY", "12345"],
# 	["Erin", "Smith", 14, "333 Top Way.", "Los Angeles", "CA", "90210"],
# 	["Bob", "Field", 15, "876 Left St.", "Memphis", "TN", "34321"],
# 	["Steve", "Target", 16, "1234 Main St.", "Miami", "FL", "12321"],
# 	["Tina", "Walton", 17, "654 Street Ave.", "Chicago", "IL", "60611"],
# 	["Mark", "Erendale", 18, "12 East St.", "Nashville", "TN", "54345"],
# 	["John", "Nowerton", 19, "678 North Ave.", "St. Louis", "MO", "67821"],
# 	["Mary", "Hornblower", 20, "9 Elder Way.", "Dallas", "TX", "88948"]
# ]


# -------------------------------REAL DATA------------------------------
csor.execute('select * from CRM')
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
                       values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), 
                       tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text='', 
                       values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), 
                       tags=('oddrow',))
    count += 1

# --------------Entry Boxes-----------
# Record likha hua
data_frame = LabelFrame(frame, text='Record')
data_frame.pack(fill='x', expand='yes', padx=20)

# First Name Label and Entry
fn_label = Label(data_frame, text='First Name')
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10, pady=10)

# Last Name Label and Entry
ln_label = Label(data_frame, text='Last Name')
ln_label.grid(row=0, column=2, padx=10, pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(row=0, column=3, padx=10, pady=10)

# ID Label and Entry
id_label = Label(data_frame, text='ID')
id_label.grid(row=0, column=4, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=5, padx=10, pady=10)

# Address Label and Entry
address_label = Label(data_frame, text='Address')
address_label.grid(row=1, column=0, padx=10, pady=10)
address_entry = Entry(data_frame)
address_entry.grid(row=1, column=1, padx=10, pady=10)

# City Label and Entry
city_label = Label(data_frame, text='City')
city_label.grid(row=1, column=2, padx=10, pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=1, column=3, padx=10, pady=10)

# State Label and Entry
state_label = Label(data_frame, text='State')
state_label.grid(row=1, column=4, padx=10, pady=10)
state_entry = Entry(data_frame)
state_entry.grid(row=1, column=5, padx=10, pady=10)

# ZipCode Label and Entry
zipcode_label = Label(data_frame, text='Zipcode')
zipcode_label.grid(row=1, column=6, padx=10, pady=10)
zipcode_entry = Entry(data_frame)
zipcode_entry.grid(row=1, column=7, padx=10, pady=10)

# --------------Functions------------------
# Clear Entries
def clear_entries():
    # Clearing Entry Boxes
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)


# Select Records
def select_record(e):
    # Clearing Entry Boxes
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)

    # Grabing selected record(number to be precise)
    selected = my_tree.focus()
    # Grab record values
    values = my_tree.item(selected, 'values')

    # Inserting Values
    fn_entry.insert(0, values[0])
    ln_entry.insert(0, values[1])
    id_entry.insert(0, values[2])
    address_entry.insert(0, values[3])
    city_entry.insert(0, values[4])
    state_entry.insert(0, values[5])
    zipcode_entry.insert(0, values[6])

def add_record():
    global count
    if count%2==0:
        my_tree.insert(parent='',index='end' ,iid=count, text='', values=(
            fn_entry.get(), ln_entry.get(), id_entry.get(), address_entry.get(), city_entry.get(), state_entry.get(), zipcode_entry.get()
        ), tags=('evenrow'))
    else:
        my_tree.insert(parent='',index='end' ,iid=count, text='', values=(
            fn_entry.get(), ln_entry.get(), id_entry.get(), address_entry.get(), city_entry.get(), state_entry.get(), zipcode_entry.get()
        ), tags=('oddrow'))
    
    # MySQL
    csor.execute("insert into CRM values('{}', '{}', {}, '{}', '{}', '{}', {})".
                 format(fn_entry.get(), ln_entry.get(), id_entry.get(), address_entry.get(), city_entry.get(), state_entry.get(), zipcode_entry.get()))
    mydata.commit()

    count += 1
    
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)

def update_record():
    selected = my_tree.focus()

    my_tree.item(selected, text='', values=(
            fn_entry.get(), ln_entry.get(), id_entry.get(), address_entry.get(), city_entry.get(), state_entry.get(), zipcode_entry.get()
        ))
    
    # MySQL
    record_id = my_tree.item(selected)['values'][1]
    csor.execute("UPDATE CRM SET first_name = ('{}'), last_name = ('{}'),id = ({}), address = ('{}'), city = ('{}'), state = ('{}'), zipcode = ('{}') WHERE id = ({})".
                 format(fn_entry.get(),ln_entry.get() ,id_entry.get(), address_entry.get(),city_entry.get(), state_entry.get(), zipcode_entry.get() ,record_id))
    mydata.commit()
    
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)
    

# Remove One Selected
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)

# Remove Selected
def remove_selected():
    x = my_tree.selection()
    for record in x:
        record_id = my_tree.item(record)['values'][1]
        # csor.execute('DELETE FROM part1 where id = ({})'.format(record_id))
        # mydata.commit()
        my_tree.delete(record)

# Remove All Record
def remove_all_record():
    for record in my_tree.get_children():
        my_tree.delete(record)

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

# -----------------------------------------------Ships-------------------------------------------------
class Ships:
    speed = 0
    # IMO Number = The International Maritime Organization (IMO) number uniquely identifies each seagoing ship. It is an important reference for tracking and managing vessels.
    def __init__(self, name, IMO_Number ,condition, navigation_status, type, Embarkation, Destination):
        self.Name = name
        self.Condition = condition
        self.Navigation_Status = navigation_status
        self.IMO_Number = IMO_Number
        self.Type = type
        self.Embarkation = Embarkation
        self.Destination = Destination

    @classmethod
    def change_condition(cls, condition):
        cls.condition = condition
    
    @classmethod
    def change_navigation_status(cls, navigation_status):
        cls.navigation_status = navigation_status

    def update_speed(self):
        self.speed = random.randint(25, 30)

# Function to update speed
def update_speed(name_of_ship):
    name_of_ship.update_speed()

Ship1 = Ships(name='Nakul', IMO_Number='134976143', condition='Good', navigation_status='On Going', type='abc'
              , Embarkation='BOM', Destination='Chennai')

print(Ship1.__dict__)
print(Ship1.speed)

Ship1.update_speed()
print(Ship1.speed)

# --------------------End-------------------
root.mainloop()