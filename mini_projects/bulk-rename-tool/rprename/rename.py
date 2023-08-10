"""This module provides the Renamer class to rename multiple files."""

import time
from pathlib import Path

from PyQt5.QtCore import QObject, pyqtSignal

# Subclass of QObject
class Renamer(QObject):
    # Define custom signals
    # Returns an integer representing the number of the currently renamed file
    # Number is used to update the progress bar
    progressed = pyqtSignal(int)
    # Returns path to the renamed file to update the list of renamed files
    renamedFile = pyqtSignal(Path)
    # When file renaming process finishes
    finished = pyqtSignal()

    def __init__(self, files, prefix):
        super().__init__()
        self._files = files
        self._prefix = prefix

    def renameFiles(self):
        # Generate a file number
        for fileNumber, file in enumerate(self._files, 1):
            # Build new filenames
            newFile = file.parent.joinpath(
                f"{self._prefix}{str(fileNumber)}{file.suffix}"
            )
            file.rename(newFile)
            # Comment this line to rename files faster
            time.sleep(0.1)
            self.progressed.emit(fileNumber)
            self.renamedFile.emit(newFile)
        # Reset the progress bar after finishing the file renaming process
        self.progressed.emit(0)
        self.finished.emit()
