


import sys
import random
import logging
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel, QPushButton, QWidget, QMessageBox
from PyQt5.QtGui import QClipboard

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def generate_id():
    id_number = random.randint(0, 99999)
    logging.info(f"PIPE ID TICKET: TDSD-{id_number:05d}")
    return f"TDSD-{id_number:05d}"

class IDWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("ID Generator")
        self.setGeometry(300, 300, 300, 150)

        # Layout and widgets
        layout = QVBoxLayout()

        self.label = QLabel("Press the button to generate an ID", self)
        layout.addWidget(self.label)

        self.generate_button = QPushButton("Generate ID", self)
        layout.addWidget(self.generate_button)
        self.generate_button.clicked.connect(self.show_id)

        self.copy_button = QPushButton("Copy to Clipboard", self)
        self.copy_button.setEnabled(False)  # Initially disabled until an ID is generated
        layout.addWidget(self.copy_button)
        self.copy_button.clicked.connect(self.copy_to_clipboard)

        self.setLayout(layout)

    def show_id(self):
        # Generate and display the ID
        self.id_number = generate_id()
        self.label.setText(f"Generated ID: {self.id_number}")
        self.copy_button.setEnabled(True)

    def copy_to_clipboard(self):
        if hasattr(self, 'id_number') and self.id_number:
            clipboard = QApplication.clipboard()
            clipboard.setText(self.id_number)
            #QMessageBox.information(self, "Copied", "ID copied to clipboard!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IDWindow()
    window.show()
    sys.exit(app.exec_())


