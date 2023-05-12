import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from View.FrmPrincipal import Ui_FrmPrincipal
from PyQt5 import QtCore
from View.Front_CadastroCliente import J_FrmCadastroCliente


class J_FormPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmPrincipal()
        self.ui.setupUi(self)
        self.ui.actionCadasta_Cliente.triggered.connect(self.abre_frmcadastrocliente)
        self.ui.actionFinalizar_Aplicativo.triggered.connect(self.close)
        self.setWindowFlags(
            QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowSystemMenuHint)

    @QtCore.pyqtSlot()
    def abre_frmcadastrocliente(self):
        self.frm_cadastracliente = J_FrmCadastroCliente()
        self.frm_cadastracliente.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = J_FormPrincipal()
    window.show()
    sys.exit(app.exec_())
