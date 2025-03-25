from PyQt5.QtWidgets import QLineEdit, QPlainTextEdit, QComboBox

def limpa_campos(self):
    # Modificado para passar uma tupla contendo as classes desejadas como o primeiro argumento
    widgets = self.findChildren((QLineEdit, QPlainTextEdit, QComboBox))

    for widget in widgets:
        # Verificar se o widget é uma instância de QComboBox antes de tentar chamá-lo
        if isinstance(widget, QComboBox):
            widget.clear()
        else:
            widget.clear()

# Exemplo de uso:
# limpa_campos(self)

'''
from PyQt5.QtWidgets import QLineEdit, QPlainTextEdit


def limpa_campos(self):
    widgets = self.findChildren((QLineEdit, QPlainTextEdit))
    for widget in widgets:
        widget.clear()
'''