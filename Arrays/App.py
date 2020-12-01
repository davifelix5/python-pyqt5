import sys
import utils
from PyQt5.Qt import QApplication, QMainWindow
from design import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setFixedSize(342, 331)
        self.numbers = [c for c in range(31)]
        # follows the index of each filter on the combo box widget
        self.filterCallbacks = [
            lambda num: True,
            lambda num: utils.is_even_number(num),
            lambda num: not utils.is_even_number(num),
            lambda num: utils.is_perfect_square(num),
        ]
        self.addBtn.clicked.connect(self.addNumber)
        self.removeBtn.clicked.connect(self.removeNumber)
        self.orderBtn.clicked.connect(self.orderNumbers)
        self.alterBtn.clicked.connect(self.alterNumber)
        self.filterOptions.currentIndexChanged.connect(self.formList)
        self.formList()

    def formList(self):
        self.resultList.clear()
        numbersToShow = self.filterNumbers(self.getFilterCallback())
        for index, number in enumerate(self.numbers):
            if number in numbersToShow:
                self.resultList.addItem(f'[{index}] -> {number}')

    def addNumber(self):
        value = self.numberValue.value()
        self.numbers.append(value)
        self.formList()

    def alterNumber(self):
        value = self.numberValue.value()
        selectedIndex = self.getSelectedListIndex()
        if selectedIndex is not None:
            self.numbers[selectedIndex] = value
            self.formList()

    def removeNumber(self):
        selectedIndex = self.getSelectedListIndex()
        if selectedIndex is not None:
            del self.numbers[selectedIndex]
            self.formList()

    def orderNumbers(self):
        self.numbers = sorted(self.numbers)
        self.formList()

    def getSelectedListIndex(self):
        try:
            selectedItem = self.resultList.selectedItems()[0]
        except IndexError:
            return None
        selectedIndex = self.resultList.row(selectedItem)
        return selectedIndex

    def getFilterCallback(self):
        return self.filterCallbacks[self.filterOptions.currentIndex()]

    def filterNumbers(self, filterCallback):
        filteredNumbers = list(filter(filterCallback, self.numbers))
        return filteredNumbers


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
