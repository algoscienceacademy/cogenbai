class QtTemplate:
    @staticmethod
    def generate_main_window() -> str:
        return '''
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt Application")
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        # Add your widgets here

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
'''

    @staticmethod
    def generate_widget() -> str:
        return '''
from PySide6.QtWidgets import QWidget, QVBoxLayout

class CustomWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        # Add your widget components here
'''
