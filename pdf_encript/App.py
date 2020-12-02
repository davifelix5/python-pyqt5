import sys
from pathlib import Path
from design import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from encrypt_pdf import encript


class PdfEncripter(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.home_path = Path.home()

        self.input_path = None
        self.output_path = None

        self.findButton.clicked.connect(self.find_file)
        self.saveBtn.clicked.connect(self.save_path)
        self.finalButton.clicked.connect(self.final)

    def find_file(self):
        input_path, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Esolha um arquivo PDF para encriptar',
            str(self.home_path),
            'PDF (*.PDF)'
        )
        self.inputFile.setText(input_path)
        self.input_path = input_path

    def save_path(self):
        output_path, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar PDF como',
            str(self.home_path),
            'PDF (*.pdf)'
        )
        self.outputFile.setText(output_path)
        self.output_path = output_path

    def final(self):

        senha = self.pwd.text()

        if not self.input_path or not self.output_path or not senha:
            msg = QMessageBox()
            msg.setText('Informe todos os dados')
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            return

        try:
            encript(self.input_path, self.output_path, senha)
        except Exception as e:
            msg = QMessageBox()
            msg.setText(e)
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setText('Arquivo salvo com sucesso')
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

            self.outputFile.setText('')
            self.inputFile.setText('')
            self.pwd.setText('')


if __name__ == '__main__':
    qt = QApplication(sys.argv)

    app = PdfEncripter()
    app.show()

    qt.exec_()
