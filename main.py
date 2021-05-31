import sys

from PIL import ImageGrab
from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication, QMessageBox

def saveFileDialog():
    options = QFileDialog.Options()
    widget = QWidget()

    image = ImageGrab.grabclipboard()
    if not hasattr(image, "save"):
        QMessageBox.critical(widget, "Error", "There is no image in the clipboard")
        return

    fileName, _ = QFileDialog.getSaveFileName(widget, "Save image", "image.png", "PNG (*.png)", options=options)

    if fileName:
        image.save(fileName, "PNG")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    saveFileDialog()
