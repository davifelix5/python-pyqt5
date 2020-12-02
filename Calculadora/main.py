import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora do Félix em Python')
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.result = False

        # LUGAR DE DIGITAR OS NÚMEROS
        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            "* {background-color: #FFF; color: #000; font-size: 30px}"
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        # BOTOES
        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1, operation=True)
        # Limpa a tela
        self.add_btn(
            QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.clear(),
            'background-color: #ff3e00'
        )

        self.add_btn(QPushButton('3'), 2, 0, 1, 1)
        self.add_btn(QPushButton('4'), 2, 1, 1, 1)
        self.add_btn(QPushButton('5'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1, operation=True)
        # Apaga um caractere
        self.add_btn(
            QPushButton('←'), 2, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1]
            ),
            'background-color: #e94b4b'
        )

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('/'), 3, 3, 1, 1, operation=True)
        self.add_btn(QPushButton(''), 3, 4, 1, 1)

        self.add_btn(QPushButton(''), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton(''), 4, 2, 1, 1)
        self.add_btn(QPushButton('*'), 4, 3, 1, 1, operation=True)
        self.add_btn(
            QPushButton('='), 4, 4, 1, 1,
            self.equals,
            'background-color: #28a23c'
        )

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan, func=None, style=None, operation=False):

        def setDisplay():
            if self.result and not operation:
                self.display.setText(
                    btn.text()
                )
            else:
                self.display.setText(
                    self.display.text() + btn.text()
                )

            self.result = False

        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not func:
            btn.clicked.connect(setDisplay)
        else:
            btn.clicked.connect(func)
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        if style:
            btn.setStyleSheet(style)
        elif not style and operation:
            btn.setStyleSheet('background-color: #756ef0')
        else:
            btn.setStyleSheet('background-color: #6ce0ed')

        if not btn.text():
            btn.setStyleSheet('')

    def equals(self):
        try:
            if self.display.text().isdigit():
                raise ValueError
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Error')
            print(e)
        finally:
            self.result = True


if __name__ == '__main__':
    qt = QApplication(sys.argv)

    calc = Calculadora()
    calc.show()

    qt.exec_()