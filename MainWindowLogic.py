from PyQt5 import QtWidgets;
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

        self.changeTextButton.clicked.connect(self.ChangeOutputTextToUserInput);

    def ExitEvent(self):
        print("exit clicked!");
        sys.exit();

    def ChangeOutputTextToUserInput(self):
        userInputStr = self.userInputLineEdit.text();
        currentOutputStr = self.outputDisplayTextBrowser.toPlainText();
        self.outputDisplayTextBrowser.setPlainText(userInputStr);
        print(f"changed text in output from {currentOutputStr} to {userInputStr}");