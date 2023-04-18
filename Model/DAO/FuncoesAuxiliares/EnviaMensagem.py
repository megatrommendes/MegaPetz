from PyQt5 import QtWidgets


def envia_mensagem(titulo, mensagem):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setText(mensagem)
    msg.setWindowTitle(titulo)
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()