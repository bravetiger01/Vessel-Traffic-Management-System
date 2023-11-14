import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class MapApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Map App")
        self.setGeometry(100, 100, 800, 600)

        # Create QWebEngineView
        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)

        # Load HTML file
        self.web_view.setUrl(QUrl.fromLocalFile(r"E:\Project CS\Vessel Traffic Management System\GUI\map.html"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapApp()
    window.show()
    sys.exit(app.exec_())
