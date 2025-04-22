import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
)
from PyQt6.QtGui import QIcon

image_path = "ch10_presenting_data_in_pyqt/icons"


class MainWindow(QWidget):
    def __init__(self):
        """Constructor for Empty Window Class."""
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(500, 300)
        self.setWindowTitle("QTreeWidget Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        tree_widget = QTreeWidget()
        tree_widget.setColumnCount(2)
        tree_widget.setHeaderLabels(["Fruit Type", "Description"])
        tree_widget.setColumnWidth(0, 160)

        category_1 = QTreeWidgetItem(
            tree_widget, ["Apples", "Edible fruit produced by an apple tree"]
        )

        apple_list = [
            [
                "Braeburn",
                "Yellow with red stripes or blush",
                f"{image_path}/braeburn.png",
            ],
            ["Empire", "Solid red", f"{image_path}/empire.png"],
            ["Ginger Gold", "Green-yellow", f"{image_path}/ginger_gold.png"],
        ]

        for i in range(len(apple_list)):
            category_1_child = QTreeWidgetItem(apple_list[i][:2])
            category_1_child.setIcon(0, QIcon(apple_list[i][2]))
            category_1.addChild(category_1_child)

        category_2 = QTreeWidgetItem(tree_widget, ["Orange", "A type of citrus fruit"])
        orange_list = [
            ["Navel", "Sweet and slightly bitter", f"{image_path}/navel.png"],
            ["Blood Orange", "Juicy and tart", f"{image_path}/blood_orange.png"],
            ["Clementine", "Usually seedless", f"{image_path}/clementine.png"],
        ]

        for i in range(len(orange_list)):
            category_2_child = QTreeWidgetItem(orange_list[i][:2])
            category_2_child.setIcon(0, QIcon(orange_list[i][2]))
            category_2.addChild(category_2_child)

        main_v_box=QVBoxLayout()
        main_v_box.addWidget(tree_widget)
        self.setLayout(main_v_box)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
