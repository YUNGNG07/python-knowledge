"""This module provides the RP Renamer application."""

import sys
from PyQt5.QtWidgets import QApplication
from .views import Window

def main():
    # Create the application
    app = QApplication(sys.argv)
    # Create and show the main window
    win = Window()
    win.show()
    # Cleanly exit application when user closes the main window
    sys.exit(app.exec())
