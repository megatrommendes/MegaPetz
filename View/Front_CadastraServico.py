from PyQt5.QtWidgets import QWidget
from View.FrmCadastraServico import Ui_FrmCadastraServico


class J_FrmCadastraServiso(QWidget):
    def __init__(self):
        super().__init__()
        self.cliente = Ui_FrmCadastraServico()
        self.ui = self.cliente
        self.ui.setupUi(self)


