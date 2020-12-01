import sys
import utils
from PyQt5.Qt import QMainWindow, QApplication
from design import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().setupUi(self)
        self.numbers = range(0, 0)
        self.filterOptions = [
            lambda num: True,
            lambda num: utils.is_even_number(num),
            lambda num: not utils.is_even_number(num),
            lambda num: utils.is_perfect_square(num),
        ]
        self.begginingSlider.valueChanged.connect(
            lambda x: self.begginingValue.setText(str(x)))
        self.endSlider.valueChanged.connect(
            lambda x: self.endValue.setText(str(x)))
        self.stepSlider.valueChanged.connect(
            lambda x: self.stepValue.setText(str(x)))
        self.submitButton.clicked.connect(self.handleSubmit)
        self.filterCombo.currentIndexChanged.connect(self.showList)

    def handleSubmit(self):
        self.count()
        self.showList()

    def count(self):
        initial = int(self.begginingValue.text())
        end = int(self.endValue.text())
        step = int(self.stepValue.text())

        step *= -1 if initial > end else 1
        end += -1 if initial > end else 1

        self.numbers = range(initial, end, step)

    def showList(self):
        self.resultList.clear()
        for number in self.numbers:
            if (self.getFilterCallback()(number)):
                self.resultList.addItem(str(number))

    def getFilterCallback(self):
        return self.filterOptions[self.filterCombo.currentIndex()]


if __name__ == "__main__":
    qt = QApplication(sys.argv)

    app = App()
    app.show()

    qt.exec_()
