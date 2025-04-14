import sys
from PyQt6.QtWidgets import QApplication, QStyleFactory

# Find out your OS's available styles
print(f"Keys: {QStyleFactory.keys()}")

# Find out the default style applied to an application
app = QApplication(sys.argv)
print(f"Default style: {app.style().name()}")
