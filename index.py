from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton;
from PyQt5.QtCore import QSize, Qt;

import sys;

from MainWindowLogic import MainWindowLogic;

def main():
    app = QApplication(sys.argv)
    ui = MainWindowLogic()
    # ui.showMaximized()
    ui.show();
    sys.exit(app.exec_())

if __name__ == "__main__":
    main();