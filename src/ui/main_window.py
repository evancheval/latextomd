from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QClipboard, QIcon
from PyQt5.QtCore import Qt, QBuffer, QIODevice
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

# Import the extract_text_from_image function
try:
    from src.mathpix import extract_text_from_image  # Adjust the import statement to match your project structure
except ImportError as e:
    print(f"Error importing extract_text_from_image: {e}")
    sys.exit(1)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("latextomd GUI")
        self.setWindowIcon(QIcon('C:/Users/evanc/source/repos/latextomd/src/images/icon.ico'))  # Set the window icon
        self.resize(840, 100)  # Set the window size to 400x400 pixels
        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove the title bar and frame
        self.move(0, 980)  # Set the window position to (100, 100)

        # self.quit_button = QPushButton("Quit", self)
        # self.quit_button.clicked.connect(self.quit_application)

        self.proceed_button = QPushButton("🚀", self)
        self.proceed_button.setFixedSize(840, 80)  # Enlarge the proceed_button
        self.proceed_button.setStyleSheet("font-size: 50px;")  # Enlarge the button text
        self.proceed_button.clicked.connect(self.proceed_on_clipboard)

        layout = QVBoxLayout()
        layout.addWidget(self.proceed_button)
        # layout.addWidget(self.quit_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def proceed_on_clipboard(self):
        self.proceed_button.setText("🔄️")  # Change the button text while processing
        clipboard = QApplication.clipboard()
        mime_data = clipboard.mimeData()
        if mime_data.hasImage():
            image = clipboard.image()
            buffer = QBuffer()
            buffer.open(QIODevice.WriteOnly)
            image.save(buffer, "PNG")
            image_data = buffer.data().data()
            extracted_text = extract_text_from_image(image_data) # Extract text from the image with MathPix API
        else:
            extracted_text = clipboard.text() # Extract text from the clipboard as there is no image
            # clipboard.setText("No image found in clipboard.")
            # self.proceed_button.setText("❌")  # Change the button text if did not succeed
        
        converted_text = latextomd(extracted_text) # Apply the latextomd function
        clipboard.setText(converted_text) # Copy the converted text to the clipboard
        self.proceed_button.setText("🚀") # Change the button text back to the original text
            
    # def quit_application(self):
    #     QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())