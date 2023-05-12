from pywebio import start_server
from pywebio.input import input
from pywebio.output import put_text, put_html
from PyQt5 import uic

class Form:
    def __init__(self):
        self.ui = uic.loadUi(r'C:\MegaPetz\View\UI\aapwebbrouse.ui')
        self.ui.submit_button.clicked.connect(self.submit)

    def submit(self):
        name = self.ui.name_input.text()
        age = self.ui.age_input.text()
        put_text(f'Name: {name}, Age: {age}')

    def run(self):
        put_html(self.ui.frameGeometry().toHtml())
        self.ui.show()

    def hello(self):
        name = input("Qual é o seu nome?")
        put_text("Olá, ", name)


if __name__ == '__main__':
    print("Iniciando o servidor...")
    form = Form()
    print("Servidor iniciado.")
    start_server(form.run, port=80)

