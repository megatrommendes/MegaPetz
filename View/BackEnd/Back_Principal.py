import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow

from Model.DAO.FuncoesAuxiliares.CancelaTab import Cancela_Tab
from View.BackEnd.Back_CadastraAlteraAnimal import J_FrmCadastraAlteraAnimal
from View.BackEnd.Back_CadastraAlteraCliente import J_FrmCadastraAlteraCliente
from View.BackEnd.Back_CadastraServico import J_FrmCadastraServico
from View.BackEnd.Back_ConsultaCliente import J_FrmConsultaCliente
from View.FontEnd.FrmPrincipal import Ui_FrmPrincipal


class J_FormPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmPrincipal()
        self.ui.setupUi(self)

        self.menuBar().setStyleSheet("""
            QMenuBar {
                background-color: rgb(110, 165, 165);
                color: white;
            }
            QMenuBar::item {
                background-color: rgb(110, 165, 165);
                color: white;
            }
            QMenu {
                background-color: rgb(110, 165, 165);
                color: white;
            }
            QMenu::item {
                background-color: rgb(110, 165, 165);
                color: white;
            }
            QMenu::item:selected {
                background-color: rgb(110, 165, 165);
                color: black;
            }
        """)

        self.ui.actionCadasta_Cliente.triggered.connect(lambda: self.abre_FrmCadastraAlteraCliente('C'))  # coloca o
        # formulário em mode de Cadastro de Cliente

        self.ui.actionAltera_Cliente.triggered.connect(lambda: self.abre_FrmCadastraAlteraCliente('A'))  # coloca o
        # formulário em mode de Anteração de cliente e retorna os dados localizados para a alteração

        self.ui.actionConsulta_Cliente.triggered.connect(lambda: self.abre_FrmConsultaCliente('CC'))  # Informa que os
        # dados retornados devem ser exibidos no formulário Consulta Cliente

        self.ui.actionCadastro_Mascote.triggered.connect(lambda: self.abre_FrmCadastraAlteraAnimal('CM'))  # Informa
        # que os dados retornados devem devem ser exibidos no formulário Cadastra Animal

        self.ui.actionCadastra_Servi_o.triggered.connect(lambda: self.abre_FrmCadastraServico())

        self.ui.actionFinalizar_Aplicativo.triggered.connect(self.close)

        self.setWindowFlags(
            QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowSystemMenuHint)

    @QtCore.pyqtSlot()
    def abre_FrmCadastraServico(self):
        self.Frm_CadastraServico = J_FrmCadastraServico()
        self.Frm_CadastraServico.show()

    @QtCore.pyqtSlot()
    def abre_FrmCadastraAlteraCliente(self, operacao):
        self.Frm_CadastraAlteraCliente = J_FrmCadastraAlteraCliente(operacao)
        self.Frm_CadastraAlteraCliente.show()

    @QtCore.pyqtSlot()
    def abre_FrmConsultaCliente(self, operacao):
        self.Frm_ConsultaCliente = J_FrmConsultaCliente(operacao)
        self.Frm_ConsultaCliente.show()

    @QtCore.pyqtSlot()
    def abre_FrmCadastraAlteraAnimal(self, operacao):
        self.Frm_CadastraAlteraAnimal = J_FrmCadastraAlteraAnimal(operacao)
        self.Frm_CadastraAlteraAnimal.show()


if __name__ == "__main__":
    app = Cancela_Tab(sys.argv)  # chama a classe "Cancela_Tab" que cancela a ação da tecla Tab
    window = J_FormPrincipal()
    window.show()
    sys.exit(app.exec_())
