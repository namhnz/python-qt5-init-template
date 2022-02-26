from PyQt5.QtWidgets import QMainWindow, QPushButton;
import sys;

from MainWindow import Ui_MainWindow;

# Create Ui logic file: https://stackoverflow.com/questions/46544780/qtdesigner-changes-will-be-lost-after-redesign-user-interface
class MainWindowLogic(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # React button click event: https://stackoverflow.com/questions/37534093/how-to-react-to-a-button-click-in-pyqt5
        self.exitButton.clicked.connect(self.ExitEvent);

    def ExitEvent(self):
        print("exit clicked!");
        sys.exit();
