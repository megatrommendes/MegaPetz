from PyQt5.QtWidgets import QLineEdit, QPlainTextEdit


def limpa_campos(self):
    widgets = self.findChildren((QLineEdit, QPlainTextEdit))
    for widget in widgets:
        widget.clear()

