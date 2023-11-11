import mysql.connector

# Connect to MySQL database
def connect_to_database():
    db = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    return db

# User login
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    role = input("Enter your role (admin/supplier): ")

    if role == "admin":
        # Perform admin login verification
        if verify_admin(username, password):
            print("Admin login successful!")
            # Call admin menu function
            admin_menu()
        else:
            print("Invalid credentials. Please try again.")

    elif role == "supplier":
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

# Admin menu
def admin_menu():
    print("\n--- Admin Menu ---")
    print("1. View ship locations")
    print("2. Update ship information")
    print("3. Add new ship")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_ship_locations()
    elif choice == "2":
        update_ship_information()
    elif choice == "3":
        add_new_ship()
    elif choice == "4":
        print("Exiting...")
    else:
        print("Invalid choice. Please try again.")
        admin_menu()

# Supplier menu
def supplier_menu(username):
    print(f"\n--- Supplier Menu ({username}) ---")
    print("1. View ship details")
    print("2. Book a ship")
    print("3. View booked ships")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_ship_details()
    elif choice == "2":
        book_ship(username)
    elif choice == "3":
        view_booked_ships(username)
    elif choice == "4":
        print("Exiting...")
    else:
        print("Invalid choice. Please try again.")
        supplier_menu(username)

# Function to view ship locations
def view_ship_locations():
    # TODO: Implement ship location retrieval and display

    # Example:
    print("--- Ship Locations ---")
    print("Ship 1 - Location: Lat: 35.6895, Lon: 139.6917")
    print("Ship 2 - Location: Lat: 51.5074, Lon: -0.1278")
    print("Ship 3 - Location: Lat: 40.7128, Lon: -74.0060")

# Function to update ship information
def update_ship_information():
    # TODO: Implement ship information update

    # Example:
    ship_id = input("Enter the ship ID: ")
    # Prompt for the fields to be updated (e.g., availability, destination, etc.)
    # Update the ship information in the database

# Function to add a new ship
def add_new_ship():
    # TODO: Implement adding a new ship

    # Example:
    ship_name = input("Enter the ship name: ")
    capacity = input("Enter the capacity: ")
    availability = input("Enter the availability: ")
    destination = input("Enter the destination: ")
    arrival = input("Enter the arrival date and time: ")
    other_details = input("Enter any other details: ")

    # Insert the ship information into the database

# Function to view ship details
def view_ship_details():
    # TODO: Implement ship details retrieval and display

    # Example:
    print("--- Ship Details ---")
    print("Ship 1 - Name: Ship A, Capacity: 100, Availability: Available")
    print("Ship 2 - Name: Ship B, Capacity: 200, Availability: Booked")
    print("Ship 3 - Name: Ship C, Capacity: 150, Availability: Available")

# Function to book a ship
def book_ship(username):
    # TODO: Implement ship booking functionality

    # Example:
    ship_id = input("Enter the ship ID to book: ")
    # Perform the booking process and update the ship availability in the database

# Function to view booked ships
def view_booked_ships(username):
    # TODO: Implement retrieving and displaying booked ships for the supplier

    # Example:
    print("--- Booked Ships ---")
    print("Supplier: ", username)
    print("Ship 2 - Name: Ship B, Capacity: 200, Destination: Port X")

# Main program flow
def main():
    print("Welcome to the Vessel Traffic Management System (VTMS)!")
    login()

# Start the program
main()
