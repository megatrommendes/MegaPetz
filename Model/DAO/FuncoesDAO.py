import re
from datetime import datetime
from PyQt5.QtGui import QFocusEvent
from PyQt5.QtWidgets import QLineEdit, QComboBox, QPlainTextEdit, QLabel
from PyQt5.QtCore import Qt, QObject
from PyQt5 import QtWidgets, QtCore
import requests


class Cancela_Tab(QtWidgets.QApplication):
    """
        Aqui, a classe Cancela_Tab é uma subclasse da classe QApplication que sobrescreve
        o método notify para interceptar os eventos de teclado e cancelar a ação da tecla Tab.
    """

    @QtCore.pyqtSlot()
    def notify(self, receiver, event):
        if event.type() == QtCore.QEvent.KeyPress and event.key() == QtCore.Qt.Key_Tab:
            return True
        return super().notify(receiver, event)


# Removendo caracteres não numéricos
@QtCore.pyqtSlot(str)
def so_numero(text):
    # Remove caracteres não numéricos
    text = ''.join(filter(str.isdigit, text))
    return text


# Formata CEP
@QtCore.pyqtSlot(str)
def formata_cep(text):
    # Remove caracteres não numéricos
    text = ''.join(filter(str.isdigit, text))

    if len(text) > 8:
        # Limita o tamanho do texto
        text = text[:8]

    formatted_text = ''
    for i in range(len(text)):
        if i == 5:
            formatted_text += '-'
        formatted_text += text[i]
    return formatted_text


# Formata Telefone
@QtCore.pyqtSlot(str)
def formata_telefone(text):
    # Remove caracteres não numéricos
    text = ''.join(filter(str.isdigit, text))

    if len(text) > 14:
        # Limita o tamanho do texto
        text = text[:14]

    formatted_text = ''
    for i in range(len(text)):
        if i == 0:
            formatted_text += '(' + text[i]
        elif i == 2:
            formatted_text += ')' + text[i]
        elif i == 7:
            formatted_text += '-' + text[i]
        else:
            formatted_text += text[i]

    return formatted_text


@QtCore.pyqtSlot(str)
def valida_documento(text):
    if len(text) == 11:
        text = formata_cpf(text)
        return text

    elif len(text) == 9:
        text = formata_rg(text)
        return text


# Formata número do RG
@QtCore.pyqtSlot(str)
def formata_rg(text):
    # Remove caracteres não numéricos
    text = ''.join(filter(str.isdigit, text))
    if len(text) > 14:
        # Limita o tamanho do texto
        text = text[:14]
    formatted_text = ''
    for i in range(len(text)):
        if i == 2:
            formatted_text += '.' + text[i]
        elif i == 5:
            formatted_text += '.' + text[i]
        elif i == 8:
            formatted_text += '-' + text[i]
        else:
            formatted_text += text[i]
    return formatted_text


# Formata CPF
@QtCore.pyqtSlot(str)
def formata_cpf(text):
    # Remove caracteres não numéricos
    text = ''.join(filter(str.isdigit, text))
    if len(text) > 14:
        # Limita o tamanho do texto
        text = text[:14]
    formatted_text = ''
    for i in range(len(text)):
        if i == 3:
            formatted_text += '.' + text[i]
        elif i == 6:
            formatted_text += '.' + text[i]
        elif i == 9:
            formatted_text += '-' + text[i]
        else:
            formatted_text += text[i]
    return formatted_text


# Format Data
@QtCore.pyqtSlot(str)
def formatar_data(text):
    # Remove caracteres não numéricos
    text = ''.join(filter(str.isdigit, text))

    if len(text) > 8:
        # Limita o tamanho do texto
        text = text[:8]

    formatted_text = ''
    for i in range(len(text)):
        if i == 2 or i == 4:
            formatted_text += '/'
        formatted_text += text[i]
    return formatted_text


# Valida Data
@QtCore.pyqtSlot(str)
def valida_data(text):
    # Verifica se a data está no formato correto (DD/MM/AAAA)
    try:
        datetime.strptime(text, '%d/%m/%Y')
        return True
    except ValueError:
        return False


# Função que recebe um objeto e um evento de foco, e define a cor de fundo e estilo do objeto com base no tipo de
# objeto e no tipo de evento
def cor_foco(obj, label, event):
    if event.type() == QFocusEvent.FocusIn:  # verifica se o evento é de foco no objeto
        if isinstance(obj, QLineEdit):  # se o objeto for uma QLineEdit
            obj.setStyleSheet(
                "QLineEdit { background-color: white; border-radius: 0px; }")  # define o estilo com cor de fundo branca
            # Localiza o QLabel correspondente usando o nome do QLineEdit
            if label is not None:
                label.setStyleSheet("QLabel { background-color: rgb(0, 0, 47); color: rgb(255, 255, 255); }")

        elif isinstance(obj, QComboBox):  # se o objeto for um QComboBox
            obj.setStyleSheet(
                "QComboBox { background-color: white; color: black; border-radius: 0px; }")  # define o estilo com
            # cor de fundo branca e cor de texto preta
            if label is not None:
                label.setStyleSheet("QLabel { background-color: rgb(0, 0, 47); color: rgb(255, 255, 255); }")

        elif isinstance(obj, QPlainTextEdit):  # se o objeto for um QPlainTextEdit
            obj.setStyleSheet(
                "QPlainTextEdit { background-color: white; color: black; border-radius: 0px; }")  # define o estilo
            # com cor de fundo branca e cor de texto preta
            if label is not None:
                label.setStyleSheet("QLabel { background-color: rgb(0, 0, 47); color: rgb(255, 255, 255); }")

    elif event.type() == QFocusEvent.FocusOut:  # verifica se o evento é de perda de foco no objeto
        if isinstance(obj, QLineEdit):  # se o objeto for uma QLineEdit
            obj.setStyleSheet("QLineEdit { background-color: rgb(110, 165, 165); color: rgb(255, 255, "
                              "255); border-radius: 0px; }")  # define o estilo com cor de fundo cinza e cor
            if label is not None:
                label.setStyleSheet("QLabel { background-color: rgb(255, 145, 10); color: rgb(255, 255, 255); }")

        elif isinstance(obj, QComboBox):  # se o objeto for um QComboBox
            obj.setStyleSheet("QComboBox { background-color: rgb(110, 165, 165); color: rgb(255, 255, "
                              "255); border-radius: 0px; }")  # define o estilo com cor de fundo cinza e cor de texto
            # branco
            obj.view().setStyleSheet(
                'QListView {background-color: white; color: black; border-radius: 0px;}')  # define o estilo da lista
            # suspensa com cor de fundo branca e cor de texto preta
            if label is not None:
                label.setStyleSheet("QLabel { background-color: rgb(255, 145, 10);  color: rgb(255, 255, 255); }")

        elif isinstance(obj, QPlainTextEdit):  # se o objeto for um QPlainTextEdit
            obj.setStyleSheet("QPlainTextEdit { background-color: rgb(110, 165, 165); "
                              "color: rgb(255, 255, 255); border-radius: 0px;}")  # define o estilo com cor de fundo
            # cinza e cor de texto branco
            if label is not None:
                label.setStyleSheet("QLabel {background-color: rgb(255, 145, 10); color: rgb(255, 255, 255); }")


def valida_campo_ant(self, event):
    # Verifica se a tecla Enter ou Return foi pressionada.
    if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
        # Procura todos os widgets que são instâncias de QObject no formulário atual.
        line_edits = self.findChildren(QObject)
        if line_edits:
            # Determina qual widget possui o foco atual.
            current_widget = self.focusWidget()

            # Verifica se o widget atual é uma instância de QLineEdit ou QComboBox.
            if isinstance(current_widget, (QLineEdit, QComboBox)):
                self.focusNextChild()


@QtCore.pyqtSlot()
def valida_campo(self, event):
    if event.key() not in [Qt.Key_Enter, Qt.Key_Return]:
        return
    current_widget = self.focusWidget()
    if not isinstance(current_widget, (QLineEdit, QComboBox, QPlainTextEdit)):
        return
    widget_name = current_widget.objectName()
    if isinstance(current_widget, QLineEdit):
        widget_text = current_widget.text()
    elif isinstance(current_widget, QComboBox):
        widget_text = current_widget.currentText()
    if not widget_name:
        recebe_mensagem("Erro de validação", "Esse campo é obrigatório, preencha por favor.")
        return
    if '0' in widget_name and '01' in widget_name:
        if valida_cpf(widget_text):
            self.focusNextChild()
        else:
            recebe_mensagem("Erro de validação", "CPF inválido, tente novamente por favor.")
            current_widget.setText('')
    elif '0' in widget_name and 'D' in widget_name:
        if valida_data(widget_text):
            self.focusNextChild()
        else:
            recebe_mensagem("Erro de validação", "Data inválida, tente novamente por favor.")
            current_widget.setText('')
    elif '0' in widget_name and '02' in widget_name:
        if widget_text:
            self.focusNextChild()
        else:
            recebe_mensagem("Erro de validação", "Esse campo é obrigatório, preencha por favor.")
            current_widget.setText('')
    elif '0' not in widget_name:
        self.focusNextChild()


@QtCore.pyqtSlot()
def consulta_cep(cep):
    # URL da API do ViaCEP para consulta de CEP
    url = f'https://viacep.com.br/ws/{cep}/json/'

    # faz uma solicitação GET para a API do ViaCEP
    response = requests.get(url)

    if response.ok:
        # extrai os dados do endereço do JSON
        endereco = response.json()
        if "erro" in endereco and endereco["erro"] == True:
            recebe_mensagem("CEP não encontrado.", "O CEP não foi localizado.")
            return '', '', '', ''
        else:
            logradouro = endereco.get('logradouro', '')
            if logradouro == '':
                recebe_mensagem("CEP não encontrado.", "O CEP não foi localizado"
                                                       ""
                                                       ".")
                return '', '', '', ''
            else:
                logradouro = endereco.get('logradouro', '')
                bairro = endereco.get('bairro', '')
                localidade = endereco.get('localidade', '')
                uf = endereco.get('uf', '')
                return logradouro, bairro, localidade, uf
    else:
        recebe_mensagem("CEP não encontrado.", "O CEP não foi localizado, por favor tente novamente.")
        return '', '', '', ''


@QtCore.pyqtSlot()
def recebe_mensagem(titulo, mensagem):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setText(mensagem)
    msg.setWindowTitle(titulo)
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()


@QtCore.pyqtSlot()
def valida_cpf(cpf):
    """
        Efetua a validação do CPF, tanto formatação quanto dígito verificadores.
        Args:
            cpf (str): CPF a ser validado
        Returns:
            bool:
                - False, quando o CPF não possuir o formato 999.999.999-99;
                - False, quando o CPF não possuir 11 caracteres numéricos;
                - False, quando os dígitos verificadores forem inválidos;
                - True, caso contrário.
        Examples:
        >>> valida_cpf('529.982.247-25')
        True
        >>> valida_cpf('52998224725')
        False
        >>> valida_cpf('111.111.111-11')
        False
        """

    # Verifica a formatação do CPF utilizando expressão regular
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        return False

    # Obtém apenas os números do CPF, ignorando pontuações
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validação do segundo dígito verificador:
    sum_of_products = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True
