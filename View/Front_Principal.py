import sys

from Model.DAO.FuncoesAuxiliares.CancelaTab import Cancela_Tab
from View.FrmPrincipal import Ui_FrmPrincipal
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication

from View.Front_CadastraAlteraCliente import J_FrmCadastraAlteraCliente
from View.Front_ConsultaCliente import J_FrmConsultaCliente


class J_FormPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmPrincipal()
        self.ui.setupUi(self)

        self.ui.actionCadasta_Cliente.triggered.connect(lambda: self.abre_FrmCadastraAlteraCliente('C'))
        self.ui.actionAltera_Cliente.triggered.connect(lambda: self.abre_FrmCadastraAlteraCliente('A'))
        self.ui.actionConsulta_Cliente.triggered.connect(lambda: self.abre_FrmConsultaCliente())
        self.ui.actionFinalizar_Aplicativo.triggered.connect(self.close)
        self.setWindowFlags(
            QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowSystemMenuHint)

    @QtCore.pyqtSlot()
    def abre_FrmCadastraAlteraCliente(self, operacao):
        self.Frm_CadastraAlteraCliente = J_FrmCadastraAlteraCliente(operacao)
        self.Frm_CadastraAlteraCliente.show()

    @QtCore.pyqtSlot()
    def abre_FrmConsultaCliente(self):
        self.Frm_ConsultaCliente = J_FrmConsultaCliente()
        self.Frm_ConsultaCliente.show()


if __name__ == "__main__":
    app = Cancela_Tab(sys.argv)  # chama a classe "Cancela_Tab" que cancela a ação da tecla Tab
    window = J_FormPrincipal()
    window.show()
    sys.exit(app.exec_())
