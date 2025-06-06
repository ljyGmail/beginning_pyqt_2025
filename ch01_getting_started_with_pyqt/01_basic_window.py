import sys
from PyQt6.QtWidgets import QApplication, QWidget


class EmptyWindow(QWidget):
    """Cunstructor for Empty Window Class"""

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application"""
        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle("Empty Window in PyQt")
        self.show()  # Display the window on the screen


# Run the program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec())
