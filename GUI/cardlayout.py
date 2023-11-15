import tkinter as tk
from tkinter import ttk

class BookedShipsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Booked Ships")
        self.root.geometry("1000x600")  # Increased width

        # Create a list of booked ships (replace this with your data)
        self.booked_ships = [
            {"name": "Ship1", "departure": "City1", "arrival": "City2", "status": "BOOKED"},
            {"name": "Ship2", "departure": "City3", "arrival": "City4", "status": "NOT BOOKED"},
            {"name": "Ship3", "departure": "City5", "arrival": "City6", "status": "BOOKED"},
            {"name": "Ship4", "departure": "City7", "arrival": "City8", "status": "BOOKED"},
            {"name": "Ship5", "departure": "City9", "arrival": "City10", "status": "NOT BOOKED"},
            {"name": "Ship6", "departure": "City11", "arrival": "City12", "status": "BOOKED"},
            {"name": "Ship7", "departure": "City13", "arrival": "City14", "status": "NOT BOOKED"},
            {"name": "Ship8", "departure": "City11", "arrival": "City12", "status": "BOOKED"},
            {"name": "Ship9", "departure": "City13", "arrival": "City14", "status": "NOT BOOKED"},
            {"name": "Ship10", "departure": "City11", "arrival": "City12", "status": "BOOKED"},
            {"name": "Ship11", "departure": "City13", "arrival": "City14", "status": "NOT BOOKED"},
            {"name": "Ship12", "departure": "City11", "arrival": "City12", "status": "BOOKED"},
            {"name": "Ship13", "departure": "City13", "arrival": "City14", "status": "NOT BOOKED"},
            {"name": "Ship14", "departure": "City11", "arrival": "City12", "status": "BOOKED"},
            {"name": "Ship15", "departure": "City13", "arrival": "City14", "status": "NOT BOOKED"},
            {"name": "Ship16", "departure": "City11", "arrival": "City12", "status": "BOOKED"},
            {"name": "Ship17", "departure": "City13", "arrival": "City14", "status": "NOT BOOKED"},
            {"name": "Ship18", "departure": "City11", "arrival": "City12", "status": "BOOKED"},
            {"name": "Ship19", "departure": "City13", "arrival": "City14", "status": "NOT BOOKED"},
            {"name": "Ship20", "departure": "City11", "arrival": "City12", "status": "BOOKED"},
            {"name": "Ship21", "departure": "City13", "arrival": "City14", "status": "NOT BOOKED"},
            {"name": "Ship22", "departure": "City11", "arrival": "City12", "status": "BOOKED"},
            {"name": "Ship23", "departure": "City13", "arrival": "City14", "status": "NOT BOOKED"},
            {"name": "Ship24", "departure": "City11", "arrival": "City12", "status": "BOOKED"},
            {"name": "Ship25", "departure": "City13", "arrival": "City14", "status": "NOT BOOKED"},
            {"name": "Ship26", "departure": "City11", "arrival": "City12", "status": "BOOKED"},
            {"name": "Ship27", "departure": "City13", "arrival": "City14", "status": "NOT BOOKED"},
            {"name": "Ship28", "departure": "City11", "arrival": "City12", "status": "BOOKED"},
            {"name": "Ship29", "departure": "City13", "arrival": "City14", "status": "NOT BOOKED"},
            {"name": "Ship30", "departure": "City11", "arrival": "City12", "status": "BOOKED"},
            {"name": "Ship31", "departure": "City13", "arrival": "City14", "status": "NOT BOOKED"},
            {"name": "Ship32", "departure": "City11", "arrival": "City12", "status": "BOOKED"},
            {"name": "Ship33", "departure": "City13", "arrival": "City14", "status": "NOT BOOKED"},
            {"name": "Ship34", "departure": "City11", "arrival": "City12", "status": "BOOKED"},
            {"name": "Ship35", "departure": "City13", "arrival": "City14", "status": "NOT BOOKED"},
            {"name": "Ship36", "departure": "City11", "arrival": "City12", "status": "BOOKED"},
            {"name": "Ship37", "departure": "City13", "arrival": "City14", "status": "NOT BOOKED"},
            {"name": "Ship38", "departure": "City11", "arrival": "City12", "status": "BOOKED"},
            {"name": "Ship39", "departure": "City13", "arrival": "City14", "status": "NOT BOOKED"},
            {"name": "Ship40", "departure": "City11", "arrival": "City12", "status": "BOOKED"},
            {"name": "Ship41", "departure": "City13", "arrival": "City14", "status": "NOT BOOKED"},
            # Add more ships as needed
        ]

        self.create_cards()

    def create_cards(self):
        # Configure the main frame to allow vertical scrolling
        canvas = tk.Canvas(self.root)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor=tk.NW)

        # Add this line to bind the scrollbar to the canvas
        frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        for i, ship in enumerate(self.booked_ships):
            card_frame = ttk.Frame(frame, padding=(20, 10), relief=tk.RAISED, borderwidth=2)
            card_frame.grid(row=i // 3, column=i % 3, padx=20, pady=10)  # Increased padding

            # Ship Name
            name_label = ttk.Label(card_frame, text=f"Ship Name: {ship['name']}", font=("Arial", 16, "bold"))  # Increased font size
            name_label.pack(anchor=tk.W)

            # Departure City
            departure_label = ttk.Label(card_frame, text=f"Departure: {ship['departure']}")
            departure_label.pack(anchor=tk.W)

            # Arrival City
            arrival_label = ttk.Label(card_frame, text=f"Arrival: {ship['arrival']}")
            arrival_label.pack(anchor=tk.W)

            # Booking Status
            status_label = ttk.Label(card_frame, text=f"Status: {ship['status']}", foreground="green" if ship['status'] == "BOOKED" else "red")
            status_label.pack(anchor=tk.W)

if __name__ == "__main__":
    root = tk.Tk()
    app = BookedShipsApp(root)
    root.mainloop()



