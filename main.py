import os
import sys

from PIL import ImageGrab
from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication, QMessageBox

def saveFileDialog():
    widget = QWidget()

    image = ImageGrab.grabclipboard()
    if not hasattr(image, "save"):
        QMessageBox.critical(widget, "Error", "There is no image in the clipboard")
        return

    desktopPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    fileName, _ = QFileDialog.getSaveFileName(widget, "Save image", f"{desktopPath}\image.png", "PNG (*.png)")

    if fileName:
        image.save(fileName, "PNG")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    saveFileDialog()
