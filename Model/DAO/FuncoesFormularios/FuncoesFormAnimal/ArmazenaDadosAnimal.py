from datetime import datetime

from Controller.AnimalCTR import AnimalCTR


def armazena_dados_animal(self, operacao, documento):
    doc = self.ui.cad_ani_01_ob_nome.text()
    nome = self.ui.cad_ani_01_ob_nome.text()
    especie = self.ui.cad_ani_05_ob_end.currentText()
    raca = self.ui.cad_anis_03_ob_raca.currentText()
    cor = self.ui.cad_ani_04_ob_cor.currentText()
    sexo = str(self.ui.cad_ani_05_ob_sexo.currentText())
    data_nascimento = self.ui.cad_ani_06_ob_nasc.text()
    idade = self.ui.cad_ani_07_ob_idade.text()
    peso = self.ui.cad_ani_02_ob_especie.text()
    mensalista = self.ui.cad_ani_09_mensalista.isChecked()
    data_cadastro = datetime.now().strftime('%d/%m/%Y')
    hora_cadastro = datetime.now().strftime('%H:%Mh')
    observacao = self.ui.cad_ani_10_obs.document().toPlainText()
    animal = AnimalCTR()

    return animal.carrega_dados_animal(operacao, documento, doc, nome, especie, raca, cor, sexo, data_nascimento,
                                       idade, peso, mensalista, data_cadastro, hora_cadastro, observacao)

