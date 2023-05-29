# Importar os módulos necessários
from PyQt5.QtWidgets import QTableView, QApplication
from PyQt5.QtCore import Qt

# Definir uma variável para controlar o tempo entre os cliques
ultimo_clique = None

def verificar_duplo_clique(index):
    global ultimo_clique

    # Obter o tempo atual
    tempo_atual = QApplication.instance().doubleClickInterval()

    # Verificar se ocorreu um clique anteriormente
    if ultimo_clique is not None and ultimo_clique.row() == index.row():
        # Calcular o intervalo de tempo desde o último clique
        intervalo = QApplication.instance().doubleClickInterval() - ultimo_clique.elapsed()

        # Verificar se o intervalo está dentro do limite para um duplo clique
        if 0 < intervalo < tempo_atual:
            # Realizar ação desejada para o duplo clique
            print("Duplo clique detectado!")

    # Salvar o clique atual como o último clique
    ultimo_clique = index
