import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Main layout
        layout = QVBoxLayout()

        # Header
        header = QLabel("Personal Finance Dashboard")
        header.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(header)

        # User Info Section
        user_info_label = QLabel("User Info:")
        user_info_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(user_info_label)

        # Adding lines to simulate user info inputs
        for _ in range(4):
            line_edit = QLineEdit()
            layout.addWidget(line_edit)

        # Functions Section
        functions_label = QLabel("Functions:")
        functions_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(functions_label)

        # Adding buttons for functions
        button_names = ["Add Weekly", "Add Monthly", "Add Annual", "Visualization", "Suggestion"]
        for name in button_names:
            button = QPushButton(name)
            layout.addWidget(button)

        # Set layout and window properties
        self.setLayout(layout)
        self.setWindowTitle("Personal Finance Dashboard")
        self.setGeometry(100, 100, 400, 300)  # Setting window size and position



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

