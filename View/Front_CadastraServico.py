from PyQt5.QtWidgets import QWidget, QLineEdit, QPlainTextEdit, QLabel

from Model.DAO.FuncoesAuxiliares.FormataReal import formata_real
from Model.DAO.FuncoesAuxiliares.MudaCorFoco import muda_cor_foco
from Model.DAO.FuncoesFormularios.FuncoesFormServico.ValidaCampoServico import valida_campo_servico
from View.FrmCadastraServico import Ui_FrmCadastraServico
from Model.DAO.FuncoesAuxiliares.FormataHora import formata_hora


class J_FrmCadastraServico(QWidget):
    def __init__(self):
        super().__init__()
        self.cliente = Ui_FrmCadastraServico()
        self.ui = self.cliente
        self.ui.setupUi(self)

        for obj in self.findChildren((QLineEdit, QPlainTextEdit)):
            # Encontra o QLabel correspondente ao QLineEdit
            label_name = obj.objectName() + '_label'
            label = obj.parent().findChild(QLabel, label_name)
            # Instala um filtro de eventos nos objetos
            obj.installEventFilter(self)
            # Define a função lambda para o evento focusIn
            obj.focusInEvent = lambda event, obj=obj, label=label: muda_cor_foco(obj, label, event)
            # Define a função lambda para o evento focusOut
            obj.focusOutEvent = lambda event, obj=obj, label=label: muda_cor_foco(obj, label, event)

        # Conecta o evento keyPressEvent do QWidget à função valida_campo
        self.keyPressEvent = lambda event: valida_campo_servico(self, event)

        self.ui.cad_serv_02_preriodo.textChanged.connect(
            lambda text: self.ui.cad_serv_02_preriodo.setText(formata_hora(text)))

        self.ui.cad_serv_03_ob_valor.textChanged.connect(
            lambda text: self.ui.cad_serv_03_ob_valor.setText(formata_real(text)))
