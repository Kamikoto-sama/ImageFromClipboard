import sys

from PIL import ImageGrab
from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication, QMessageBox

def saveFileDialog():
    options = QFileDialog.Options()
    widget = QWidget()

    img = ImageGrab.grabclipboard()
    if not img:
        QMessageBox.critical(widget, "Error", "There is no image in the clipboard")
        return

    fileName, _ = QFileDialog.getSaveFileName(widget, "Save image", "image.png", "PNG (*.png)", options=options)

    if fileName:
        img.save(fileName, "PNG")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    saveFileDialog()
