from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QClipboard
import sys
import os

# Ensure the path is correctly set
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.append(parent_dir)

# Import the latextomd function
try:
    from src.latextomd import latextomd  # Adjust the import statement to match your project structure
except ImportError as e:
    print(f"Error importing latextomd: {e}")
    sys.exit(1)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("latextomd GUI")
        self.resize(960, 100)  # Set the window size to 400x400 pixels

        # self.quit_button = QPushButton("Quit", self)
        # self.quit_button.clicked.connect(self.quit_application)

        self.copy_button = QPushButton("🚀", self)
        self.copy_button.setFixedSize(960, 100)  # Enlarge the copy_button
        self.copy_button.setStyleSheet("font-size: 70px;")  # Enlarge the button text
        self.copy_button.clicked.connect(self.proceed_on_clipboard)

        layout = QVBoxLayout()
        layout.addWidget(self.copy_button)
        # layout.addWidget(self.quit_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def proceed_on_clipboard(self):
        clipboard = QApplication.clipboard()
        input_text = clipboard.text()
        output_text = latextomd(input_text)  # Apply the latextomd function
        clipboard.setText(output_text)

    # def quit_application(self):
    #     QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())