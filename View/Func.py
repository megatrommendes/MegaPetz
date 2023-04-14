import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QComboBox
from PyQt5.QtCore import Qt, QObject
from PyQt5 import QtWidgets

# Verifica se a tecla pressionada é "ENTER", o tipo do campo "QLineEdit" ou "QComboBox"
# e muda o foco para o proximo campo
def keyEnter(self, event):
    if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
        line_edits = self.findChildren(QObject)
        if line_edits:
            current_widget = self.focusWidget()
            if isinstance(current_widget, QLineEdit) or (current_widget, QComboBox):
                for widget in self.findChildren(QtWidgets.QWidget):
                    nome = widget.objectName()
                    posicao = nome.find('0')
                    if posicao != -1:
                        me
                        self.focusNextChild()
"""
texto = "Esta é uma string de exemplo."
posicao = texto.find('a')
if posicao != -1:
    print(f"A letra 'a' foi encontrada na posição {posicao}.")
else:
    print("A letra 'a' não foi encontrada na string.")
"""
