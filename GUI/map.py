import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import mysql.connector as mysql

class MapApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Map App")
        self.setGeometry(100, 100, 800, 600)

        # Create QWebEngineView
        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)

        # Load HTML file
        self.web_view.setUrl(QUrl.fromLocalFile(r"\map.html"))

        # Connect to MySQL
        self.connection = mysql.connect(
            host="localhost",
            user="root",
            password="nakuldesai2510",
            database="vtms"
        )

        

        # Fetch ship details from MySQL
        self.ships = self.fetch_ships()
        
        self.update_map()

    def fetch_ships(self):
        # Fetch ship details from MySQL
        query = "SELECT Name, Embarkation FROM SHIPDATA;"
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()

    def update_map(self):
        # Loop through ships and create markers
        js_commands = []
        
        print(self.ships)

        for ship in self.ships:
            # Assuming the fetched data has 'Name' and 'Embarkation' fields
            name, embarkation = ship['Name'], ship['Embarkation']
            

            # Fetch latitude and longitude from the 'Embarkation' city (you need to implement this)
            latitude, longitude = self.fetch_coordinates(embarkation)
            

            # Create JavaScript code for adding a marker
            js_command = f"L.marker([{latitude}, {longitude}]).addTo(mymap).bindPopup('{name}');"
            js_commands.append(js_command)
            

        # Join all JavaScript commands into a single string
        js_code = "\n".join(js_commands)
        

        # Execute JavaScript code in the WebView
        self.web_view.page().runJavaScript(js_code)
        print('hello')

    def fetch_coordinates(self, city):
        # Implement logic to fetch latitude and longitude from the city (you need to implement this)
        # This could involve calling a geocoding API or using a library to convert city names to coordinates.
        # For simplicity, let's assume it returns static coordinates.
        return 18.9750, 72.8258

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapApp()
    window.show()
    sys.exit(app.exec_())
