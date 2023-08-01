"""Simple Hello, World example with PyQt6"""

import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# Developers often pass sys.argc to the constructor of QApplication
# The object contains the list of command-line arguments passed into a Python script
app = QApplication([])

window = QWidget()
window.setWindowTitle("PyQt App")
# x, y (screen coordinates where window will be placed), width, height
window.setGeometry(100, 100, 280 ,80)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60, 15)

window.show()
sys.exit(app.exec())
