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

# Function to simulate the passage of time
def simulate_time_passage():
    db = connect_to_database()
    cursor = db.cursor()

    # Get current system time
    current_time = datetime.now()

    # Update ships' statuses based on timestamps
    update_ships_query_ = f"UPDATE ships SET current_status = 'At Port', goods_status = 'Unloaded', arrival_time = '{current_time}' WHERE arrival_time <= '{current_time}'"
    cursor.execute(update_ships_query_)

    # Update ships' destinations and load goods if the ship is at port and there is demand
    update_ships_departure_query_ = f"""
        UPDATE ships
        SET current_status = 'In Transit', goods_status = 'Loaded',
            departure_time = '{current_time}', arrival_time = '{(current_time + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')}'
        WHERE current_status = 'At Port' AND port_name IN (
            SELECT port_name FROM demand WHERE demand > 0 AND docked_ships < dock_limit
        )
    """
    cursor.execute(update_ships_departure_query_)

    db.commit()
    db.close()


def simulate_traffic_clearance():
    db = connect_to_database()
    cursor = db.cursor()

    # Update ships' statuses to 'Unloading' after a delay of 1 hour
    update_ships_unloading_query_ = f"""
        UPDATE ships
        SET current_status = 'Unloading', goods_status = 'Unloading'
        WHERE current_status = 'At Port' AND arrival_time + INTERVAL 1 HOUR <= NOW()
    """
    cursor.execute(update_ships_unloading_query_)

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
    while True:
        print(f"\n--- Supplier Menu ({username}) ---")
        print("1. View available ships")
        print("2. View ship details")
        print("3. View ship route")
        print("4. Book a ship")
        print("5. View booked ships")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_available_ships()
        elif choice == "2":
            ship_id = input("Enter the ship ID: ")
            view_ship_details(ship_id)
        elif choice == "3":
            ship_id = input("Enter the ship ID: ")
            view_ship_route(ship_id)
        elif choice == "4":
            book_ship(username)
        elif choice == "5":
            view_booked_ships(username)
        elif choice == "6":
            print("Exiting...")
            exit()
        else:
            print("Invalid choice. Please try again.")

# -------------------------------------Admin Functions-----------------------------

# Function to view ships at the port
def view_ships_at_port(port_name):
    query_ = f"SELECT * FROM ships WHERE port_name = '{port_name}' AND current_status = 'At Port'"
    display_results(query_)

# Function to view arriving ships
def view_arriving_ships(port_name):
    query_ = f"SELECT * FROM ships WHERE port_name = '{port_name}' AND current_status = 'Arriving'"
    display_results(query_)

# Function to view unloading ships
def view_unloading_ships(port_name):
    query_ = f"SELECT * FROM ships WHERE port_name = '{port_name}' AND current_status = 'Unloading'"
    display_results(query_)

# Function to view ship information
def view_ship_information():
    ship_id = input("Enter the ship ID: ")
    query_ = f"SELECT * FROM ships WHERE ship_id = {ship_id}"
    display_results(query_)

# Function to view goods status
def view_goods_status(port_name):
    query_ = f"SELECT g.*, s.name as ship_name FROM goods g JOIN ships s ON g.ship_id = s.ship_id WHERE s.port_name = '{port_name}'"
    display_results(query_)

# Helper function to execute and display query_ results
def display_results(query__):
    db = connect_to_database()
    cursor = db.cursor()
    cursor.execute(query__)
    result = cursor.fetchall()
    if result:
        headers = [desc[0] for desc in cursor.description]
        print(tabulate(result, headers=headers, tablefmt='pretty'))
    else:
        print("No results found.")
    db.close()

# --------------------------------------------Supplier Functions---------------------------------
# Function to view available ships
# Function to view available ships
def view_available_ships():
    db = connect_to_database()
    cursor = db.cursor()
    query = "SELECT ship_id, name, capacity, IMO, current_status, port_name, departure_time, arrival_time, goods_type_id FROM ships WHERE current_status = 'At Port' AND ship_id NOT IN (SELECT ship_id FROM bookings)"
    cursor.execute(query)
    available_ships = cursor.fetchall()
    db.close()

    if available_ships:
        headers = [desc[0] for desc in cursor.description]
        print(tabulate(available_ships, headers=headers, tablefmt='pretty'))
    else:
        print("No ships are currently available at the port.")


# Function to view ship details
def view_ship_details(ship_id):
    db = connect_to_database()
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM ships WHERE ship_id = {ship_id}")
    ship_data = cursor.fetchone()
    if ship_data:
        print("\nShip Details:")
        print(f"Ship ID: {ship_data[0]}")
        print(f"Name: {ship_data[1]}")
        print(f"Capacity: {ship_data[2]}")
        print(f"IMO: {ship_data[3]}")
        print(f"Current Status: {ship_data[4]}")
        print(f"Port Name: {ship_data[5]}")
        print(f"Goods Status: {ship_data[6]}")
        print(f"Departure Time: {ship_data[7]}")
        print(f"Arrival Time: {ship_data[8]}")
    else:
        print("Ship not found.")
    db.close()

# Function to view ship route
def view_ship_route(ship_id):
    db = connect_to_database()
    cursor = db.cursor()
    cursor.execute(f"SELECT port_name, arrival_time FROM ships WHERE ship_id = {ship_id} ORDER BY arrival_time")
    route_data = cursor.fetchall()
    if route_data:
        print("\nShip Route:")
        for port, arrival_time in route_data:
            print(f"{port} - Arrival Time: {arrival_time}")
    else:
        print("Ship not found.")
    db.close()

# Function to book a ship
def book_ship(username):
    view_available_ships()
    ship_id = input("Enter the ship ID you want to book: ")

    # Check if the ship is available
    if is_ship_available(ship_id):
        # Add logic to create a booking record in the database
        create_booking(username, ship_id)
        print(f"Booking confirmed! You have booked Ship ID {ship_id}.")
    else:
        print("Ship not available for booking.")

# Function to create a booking record
def create_booking(username, ship_id):
    db = connect_to_database()
    cursor = db.cursor()
    booking_time = datetime.now()
    insert_booking_query = f"INSERT INTO bookings (supplier_username, ship_id, booking_time) VALUES ('{username}', {ship_id}, '{booking_time}')"

    # Update the ship status to 'Booked'
    try:
        cursor.execute(insert_booking_query)
        update_ship_status_query = f"UPDATE ships SET current_status = 'Booked' WHERE ship_id = {ship_id}"
        cursor.execute(update_ship_status_query)
    except mysql.connector.errors.IntegrityError:
        print('Ship Already Booked')
    finally:
        db.commit()
        db.close()


# Function to check if the ship is available for booking
def is_ship_available(ship_id):
    db = connect_to_database()
    cursor = db.cursor()
    cursor.execute(f"SELECT ship_id FROM ships WHERE ship_id = {ship_id} AND current_status = 'At Port'")
    result = cursor.fetchone()
    db.close()
    return result is not None

# Function to view booked ships for a supplier
def view_booked_ships(username):
    db = connect_to_database()
    cursor = db.cursor()
    cursor.execute(f"SELECT DISTINCT b.*, s.name as ship_name FROM bookings b JOIN ships s ON b.ship_id = s.ship_id WHERE b.supplier_username = '{username}'")
    booked_ships = cursor.fetchall()
    if booked_ships:
        print("\nBooked Ships:")
        for booking in booked_ships:
            ship_name_index = cursor.column_names.index('ship_name')
            booking_time_index = cursor.column_names.index('booking_time')
            print(f"Ship Name: {booking[ship_name_index]}")
            print(f"Booking Time: {booking[booking_time_index]}")
            print("--------------")
    else:
        print("No booked ships found.")
    db.close()

# Main program flow
def main():
    print("-----------------------Welcome to the Vessel Traffic Management System (VTMS)!--------------------")
    login()

# Start the program
main()
