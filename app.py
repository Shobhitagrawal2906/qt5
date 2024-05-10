import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog
from image_embeddings import ImageEmbeddings

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.tensor_object = ImageEmbeddings()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("File Selector")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: navy;")

        layout = QVBoxLayout()

        self.select_button = QPushButton("Select File")
        self.select_button.setStyleSheet("background-color: blue; color: white; font: bold 12pt Arial;")
        self.select_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_button)

        self.select_multiple_button = QPushButton("Select Multiple Files")
        self.select_multiple_button.setStyleSheet("background-color: green; color: white; font: bold 12pt Arial;")
        self.select_multiple_button.clicked.connect(self.select_multiple_files)
        layout.addWidget(self.select_multiple_button)

        quit_button = QPushButton("Quit")
        quit_button.setStyleSheet("background-color: blue; color: white; font: bold 12pt Arial;")
        quit_button.clicked.connect(self.close)
        layout.addWidget(quit_button)

        self.setLayout(layout)

    def select_file(self):
    
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Please select a file:", 
            os.getcwd()
        )
        if file_path:
            self.tensor_object.calculate_tensor(file_path)

    def select_multiple_files(self):
        # Open a file dialog to select multiple files
        file_paths, temp = QFileDialog.getOpenFileNames(
            self, 
            "Please select multiple files:", 
            os.getcwd()
        )
        for file_path in file_paths:
            self.tensor_object.calculate_tensor(file_path)

def main():
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()