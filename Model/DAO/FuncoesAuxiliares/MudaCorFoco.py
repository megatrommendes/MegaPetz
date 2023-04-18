from PyQt5.QtGui import QFocusEvent
from PyQt5.QtWidgets import QComboBox, QLineEdit, QPlainTextEdit

# Função que recebe um objeto e um evento de foco, e define a cor de fundo e estilo do objeto com base no tipo de
# objeto e no tipo de evento
def muda_cor_foco(obj, label, event):
    if event.type() == QFocusEvent.FocusIn:  # verifica se o evento é de foco no objeto
        if isinstance(obj, QLineEdit):  # se o objeto for uma QLineEdit
            obj.setStyleSheet(
                "QLineEdit { background-color: white; border-radius: 0px; }")  # define o estilo com cor de fundo branca
            # Localiza o QLabel correspondente usando o nome do QLineEdit
            label.setStyleSheet("QLabel { background-color: rgb(0, 0, 47); color: rgb(255, 255, 255); }")

        elif isinstance(obj, QComboBox):  # se o objeto for um QComboBox
            obj.setStyleSheet(
                "QComboBox { background-color: white; color: black; border-radius: 0px; }")  # define o estilo com
            # cor de fundo branca e cor de texto preta
            label.setStyleSheet("QLabel { background-color: rgb(0, 0, 47); color: rgb(255, 255, 255); }")

        elif isinstance(obj, QPlainTextEdit):  # se o objeto for um QPlainTextEdit
            obj.setStyleSheet(
                "QPlainTextEdit { background-color: white; color: black; border-radius: 0px; }")  # define o estilo
            # com cor de fundo branca e cor de texto preta
            label.setStyleSheet("QLabel { background-color: rgb(0, 0, 47); color: rgb(255, 255, 255); }")

    elif event.type() == QFocusEvent.FocusOut:  # verifica se o evento é de perda de foco no objeto
        if isinstance(obj, QLineEdit):  # se o objeto for uma QLineEdit
            obj.setStyleSheet("QLineEdit { background-color: rgb(110, 165, 165); color: rgb(255, 255, "
                              "255); border-radius: 0px; }")  # define o estilo com cor de fundo cinza e cor
            label.setStyleSheet("QLabel { background-color: rgb(255, 145, 10); color: rgb(255, 255, 255); }")

        elif isinstance(obj, QComboBox):  # se o objeto for um QComboBox
            obj.setStyleSheet("QComboBox { background-color: rgb(110, 165, 165); color: rgb(255, 255, "
                              "255); border-radius: 0px; }")  # define o estilo com cor de fundo cinza e cor de texto
            # branco
            obj.view().setStyleSheet(
                'QListView {background-color: white; color: black; border-radius: 0px;}')  # define o estilo da lista
            # suspensa com cor de fundo branca e cor de texto preta
            label.setStyleSheet("QLabel { background-color: rgb(255, 145, 10);  color: rgb(255, 255, 255); }")

        elif isinstance(obj, QPlainTextEdit):  # se o objeto for um QPlainTextEdit
            obj.setStyleSheet("QPlainTextEdit { background-color: rgb(110, 165, 165); "
                              "color: rgb(255, 255, 255); border-radius: 0px;}")  # define o estilo com cor de fundo
            # cinza e cor de texto branco
            label.setStyleSheet("QLabel {background-color: rgb(255, 145, 10); color: rgb(255, 255, 255); }")