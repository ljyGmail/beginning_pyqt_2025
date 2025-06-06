import sys, random
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon

image_path = "ch05_menus_toolbars_and_more/images"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(200, 200)
        self.setWindowTitle("Changing Icons Example")
        self.setWindowIcon(QIcon(f"{image_path}/pyqt_logo.png"))

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        info_label = QLabel("Click on the button and select a fruit.")
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.images = [
            f"{image_path}/1_apple.png",
            f"{image_path}/2_pineapple.png",
            f"{image_path}/3_watermelon.png",
            f"{image_path}/4_banana.png",
        ]

        self.icon_button = QPushButton()
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(60, 60))
        self.icon_button.clicked.connect(self.changeButtonIcon)

        # Create vertical layout and add widgets
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(info_label)
        main_v_box.addWidget(self.icon_button)

        # Set main layout of window
        container = QWidget()
        container.setLayout(main_v_box)
        self.setCentralWidget(container)

    def changeButtonIcon(self):
        """When the button is clicked, change the icon to
        a different random icon from the image list."""
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(60, 60))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
