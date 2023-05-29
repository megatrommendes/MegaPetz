from PyQt5.QtGui import QFocusEvent
from PyQt5.QtWidgets import QComboBox, QLineEdit, QPlainTextEdit, QCheckBox


# Função que recebe um objeto e um evento de foco, e define a cor de fundo e estilo do objeto com base no tipo de
# objeto e no tipo de evento
def muda_cor_foco(obj, label, event):
    if event.type() == QFocusEvent.FocusIn:  # verifica se o evento é de foco no objeto
        if isinstance(obj, QLineEdit):  # se o objeto for uma QLineEdit
            obj.setStyleSheet(
                "QLineEdit { background-color: white; border-radius: 3px; border-style: solid; border-width: 1px;}")  # define o estilo com cor de fundo branca
            # Localiza o QLabel correspondente usando o nome do QLineEdit
            label.setStyleSheet("QLabel { background-color: rgb(0, 0, 47); color: rgb(255, 255, 255); border-radius: "
                                "3px; }")

        elif isinstance(obj, QComboBox):  # se o objeto for um QComboBox
            obj.setStyleSheet(
                "QComboBox { background-color: white; color: black; border-radius: 0px; border-radius: 3px;}")
            label.setStyleSheet("QLabel { background-color: rgb(0, 0, 47); color: rgb(255, 255, 255); border-radius: "
                                "3px; }")

        elif isinstance(obj, QPlainTextEdit):  # se o objeto for um QPlainTextEdit
            obj.setStyleSheet(
                "QPlainTextEdit { background-color: white; color: black; border-radius: 3px; }")
            label.setStyleSheet("QLabel { background-color: rgb(0, 0, 47); color: rgb(255, 255, 255); border-radius: "
                                "3px; }")

        elif isinstance(obj, QCheckBox):  # se o objeto for um QCheckBox
            obj.setStyleSheet(
                "QCheckBox { background-color: white; color: black; border-radius: 3px; }")
            label.setStyleSheet("QLabel { background-color: rgb(0, 0, 47); color: rgb(255, 255, 255); border-radius: "
                                "3px; }")

    elif event.type() == QFocusEvent.FocusOut:  # verifica se o evento é de perda de foco no objeto
        if isinstance(obj, QLineEdit):  # se o objeto for uma QLineEdit
            obj.setStyleSheet("QLineEdit { color: rgb(255, 255, 255); background-color: transparent;"
                              " border-style: solid; border-width: 1px;  border-color: rgb(103, 120, 138);"
                              " border-radius: 3px; }")  # define o estilo com cor de fundo cinza e cor de texto branco
            label.setStyleSheet(
                "QLabel { color: rgb(255, 255, 255); background-color:rgb(110, 165, 165);; border-radius: 3px; }")

        elif isinstance(obj, QComboBox):  # se o objeto for um QComboBox
            obj.setStyleSheet("QComboBox { color: rgb(255, 255, 255); background-color: transparent;"
                              " border-style: solid; border-width: 1px;  border-color: rgb(103, 120, 138);"
                              " border-radius: 3px; }")
            obj.view().setStyleSheet('QListView { background-color: white; color: black; border-radius: 0px; }')
            label.setStyleSheet(
                "QLabel { background-color:rgb(110, 165, 165); color: rgb(255, 255, 255); border-radius: 3px; }")

        elif isinstance(obj, QPlainTextEdit):  # se o objeto for um QPlainTextEdit
            obj.setStyleSheet("QPlainTextEdit { color: rgb(255, 255, 255); background-color: transparent;"
                              " border-style: solid; border-width: 1px;  border-color: rgb(103, 120, 138);"
                              " border-radius: 3px; }")
            label.setStyleSheet("QLabel { background-color:rgb(110, 165, 165);  color: rgb(255, 255, 255); }")

        elif isinstance(obj, QCheckBox):  # se o objeto for um QCheckBox
            obj.setStyleSheet("QCheckBox { color: rgb(255, 255, 255); background-color: transparent;"
                              " border-style: solid; border-width: 1px;  border-color: rgb(103, 120, 138);"
                              " border-radius: 3px; }")
            label.setStyleSheet(
                "QLabel { background-color:rgb(110, 165, 165); color: rgb(255, 255, 255); border-radius: 3px; }")
