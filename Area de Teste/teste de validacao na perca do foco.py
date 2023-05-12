import sys
from PyQt5.QtWidgets import QApplication, QDialog, QFormLayout, QLineEdit, QPushButton


class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QFormLayout(self)
        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        self.submit_button = QPushButton('Submit')
        layout.addRow('Name:', self.name_input)
        layout.addRow('Age:', self.age_input)
        layout.addRow('', self.submit_button)
        self.submit_button.clicked.connect(self.submit)

    def submit(self):
        name = self.name_input.text()
        age = self.age_input.text()
        print(f'Name: {name}, Age: {age}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())
