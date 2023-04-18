from PyQt5 import QtWidgets, QtCore


class Cancela_Tab(QtWidgets.QApplication):
    #  Aqui, a classe Cancela_Tab é uma subclasse da classe QApplication que sobrescreve
    #  o método notify para interceptar os eventos de teclado e cancelar a ação da tecla Tab.
    @QtCore.pyqtSlot()
    def notify(self, receiver, event):
        if event.type() == QtCore.QEvent.KeyPress and event.key() == QtCore.Qt.Key_Tab:
            return True
        return super().notify(receiver, event)