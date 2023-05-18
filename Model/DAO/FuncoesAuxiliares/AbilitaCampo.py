from PyQt5.QtWidgets import QLineEdit


def abilita_campo(self):
    widgets = self.findChildren(QLineEdit)
    for widget in widgets:
        widget.setEnabled(True)
