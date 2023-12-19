import mysql.connector
from tabulate import tabulate
from datetime import datetime, timedelta

# Connect to MySQL database
def connect_to_database():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="nakuldesai2510",
        database="vtms"
    )
    return db

# Function to get a list of available ports
def get_available_ports():
    db = connect_to_database()
    cursor = db.cursor()
    cursor.execute("SELECT DISTINCT port_name FROM ships ORDER BY port_name")
    ports = [port[0] for port in cursor.fetchall()]
    db.close()
    return ports

def simulate_time_passage():
    db = connect_to_database()
    cursor = db.cursor()

    # Get current system time
    current_time = datetime.now()

    # Update ships' statuses based on timestamps
    update_ships_query = f"UPDATE ships SET current_status = 'At Port', goods_status = 'Unloaded' WHERE arrival_time <= '{current_time}'"
    cursor.execute(update_ships_query)

    # Update ships' destinations and load goods if the ship is at port
    update_ships_departure_query = f"UPDATE ships SET current_status = 'In Transit', goods_status = 'Loaded', departure_time = '{current_time}', arrival_time = '{current_time + timedelta(days=1)}' WHERE current_status = 'At Port'"
    cursor.execute(update_ships_departure_query)

    db.commit()
    db.close()

# User login
def login():
    aos = input('Are you Admin Or Supplier?(Admin/Supplier): ')
    if aos.lower() == "admin":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        # Perform admin login verification
        if verify_admin(username, password):
            print("Admin login successful!")
            # Call admin menu function
            admin_menu()
        else:
            print("Invalid credentials. Please try again.")

    elif aos.lower() == "supplier":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        # Perform supplier login verification
        if verify_supplier(username, password):
            print("Supplier login successful!")
            # Call supplier menu function
            supplier_menu(username)
        else:
            print("Invalid credentials. Please try again.")

    else:
        print("Invalid role. Please try again.")

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
        db.close()
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
        db.close()
        return result is None


# Admin menu
def admin_menu():
    simulate_time_passage()
    print("\n---------- Admin Menu -----------")
    print("1. Choose Port")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        ports = get_available_ports()
        if ports:
            print("Available Ports:")
            for i, port in enumerate(ports, 1):
                print(f"{i}. {port}")

            port_choice = int(input("Enter the number of the port: "))
            if 1 <= port_choice <= len(ports):
                selected_port = ports[port_choice - 1]
                admin_menu_for_port(selected_port)
            else:
                print("Invalid port choice. Please try again.")
                admin_menu()
        else:
            print("No ports available. Please check your database.")
            admin_menu()

    elif choice == "2":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")
        admin_menu()

def admin_menu_for_port(port_name):
    while True:
        print(f"\n---------- Admin Menu for Port {port_name} -----------")
        print("1. View ships at port")
        print("2. View arriving ships")
        print("3. View unloading ships")
        print("4. View ship information")
        print("5. View goods status")
        print("6. Change Port")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_ships_at_port(port_name)
        elif choice == "2":
            view_arriving_ships(port_name)
        elif choice == "3":
            view_unloading_ships(port_name)
        elif choice == "4":
            view_ship_information()
        elif choice == "5":
            view_goods_status(port_name)
        elif choice == "6":
            admin_menu()
        elif choice == "7":
            print("Exiting...")
            exit()
        else:
            print("Invalid choice. Please try again.")

# Supplier menu
def supplier_menu(username):
    print(f"\n--- Supplier Menu ({username}) ---")
    # print("1. View ship details")
    # print("2. Book a ship")
    # print("3. View booked ships")
    # print("4. Exit")

    # choice = input("Enter your choice: ")

    # if choice == "1":
    #     view_ship_details()
    # elif choice == "2":
    #     book_ship(username)
    # elif choice == "3":
    #     view_booked_ships(username)
    # elif choice == "4":
    #     print("Exiting...")
    # else:
    #     print("Invalid choice. Please try again.")
    #     supplier_menu(username)

# Function to view ships at the port
def view_ships_at_port(port_name):
    query = f"SELECT * FROM ships WHERE port_name = '{port_name}' AND current_status = 'At Port'"
    display_results(query)

# Function to view arriving ships
def view_arriving_ships(port_name):
    query = f"SELECT * FROM ships WHERE port_name = '{port_name}' AND current_status = 'Arriving'"
    display_results(query)

# Function to view unloading ships
def view_unloading_ships(port_name):
    query = f"SELECT * FROM ships WHERE port_name = '{port_name}' AND current_status = 'Unloading'"
    display_results(query)

# Function to view ship information
def view_ship_information():
    ship_id = input("Enter the ship ID: ")
    query = f"SELECT * FROM ships WHERE ship_id = {ship_id}"
    display_results(query)

# Function to view goods status
def view_goods_status(port_name):
    query = f"SELECT g.*, s.name as ship_name FROM goods g JOIN ships s ON g.ship_id = s.ship_id WHERE s.port_name = '{port_name}'"
    display_results(query)

# Helper function to execute and display query results
def display_results(query):
    db = connect_to_database()
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()

    if result:
        headers = [desc[0] for desc in cursor.description]
        print(tabulate(result, headers=headers, tablefmt='pretty'))
    else:
        print("No results found.")

# Main program flow
def main():
    print("-----------------------Welcome to the Vessel Traffic Management System (VTMS)!--------------------")
    login()

# Start the program
main()
