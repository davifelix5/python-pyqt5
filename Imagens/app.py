import sys
from pathlib import Path
from design import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap


class ChangeImage(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.home_path = Path.home()
        self.selected_img = None
        self.new_img = None
        self.openBtn.clicked.connect(self.open_img)
        self.changeButton.clicked.connect(self.change_img)
        self.saveButton.clicked.connect(self.save)

        self.msg = QMessageBox()
        self.msg.setWindowTitle('Error')
        self.msg.setText('Você ainda não selecionou nenhuma imagem')
        self.msg.setIcon(QMessageBox.Information)

    def open_img(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Open image',
            str(self.home_path),
            'PNG (*.png);;JPG (*.jpg);;JPEG (*.jpeg)'
        )
        self.pathInput.setText(imagem)
        self.selected_img = QPixmap(imagem)
        self.imgArea.setPixmap(self.selected_img)

        self.widthInput.setText(
            str(self.selected_img.width())
        )

        self.heightInput.setText(
            str(self.selected_img.height())
        )

    def change_img(self):
        if not self.selected_img:
            self.msg.exec_()
            return
        new_width = int(self.widthInput.text())
        self.new_img = self.selected_img.scaledToWidth(new_width)
        self.imgArea.setPixmap(self.new_img)
        self.widthInput.setText(str(self.new_img.width()))
        self.heightInput.setText(str(self.new_img.height()))

    def save(self):
        if not self.new_img:
            self.msg.exec_()
            return
        new_path, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Save Image As',
            str(self.home_path),
            'PNG (*.png)'
        )
        self.new_img.save(new_path, 'PNG')


if __name__ == '__main__':
    qt = QApplication(sys.argv)

    app = ChangeImage()
    app.show()

    qt.exec_()
