from Model.DAO.FuncoesDAO import Cancela_Tab
from View.FormCapturaImagemCliente import Ui_formcapturaimagemcliente
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QImage, QPixmap
import cv2
from PyQt5.QtCore import QTimer, Qt
import sys

class J_FormCapturaImagemCliente(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_formcapturaimagemcliente()
        self.ui.setupUi(self)

        # Inicializa a câmera
        self.camera = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)

        # Cria um layout para o QLabel que exibe a imagem
        self.imagemcamera_layout = QHBoxLayout()
        self.ui.imagemcamera_label.setLayout(self.imagemcamera_layout)

        # Adiciona o QLabel ao QVBoxLayout e centraliza-o
        self.imagemcamera_vbox = QVBoxLayout()
        self.imagemcamera_vbox.addWidget(self.ui.imagemcamera_label)
        self.imagemcamera_vbox.setAlignment(Qt.AlignCenter)
        self.ui.imagemcamera_label.setLayout(self.imagemcamera_vbox)

    def update_frame(self):
        # Atualiza o frame da câmera
        ret, frame = self.camera.read()
        if ret:
            self.ui.camera_image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888).rgbSwapped()
            pixmap = QPixmap.fromImage(self.ui.camera_image)
            pixmap = pixmap.scaled(self.ui.imagemcamera_label.size(), Qt.KeepAspectRatio)
            self.ui.imagemcamera_label.setPixmap(pixmap)

    def captura_image(self):
        # Captura uma imagem e exibe no QLabel
        ret, frame = self.camera.read()
        if ret:
            self.ui.captureda_image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888).rgbSwapped()
        # Atualiza o frame da câmera
        ret, frame = self.camera.read()
        if ret:
            self.ui.camera_image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888).rgbSwapped()
            self.ui.imagemcamera_label.setPixmap(QPixmap.fromImage(self.ui.camera_image))

    def closeEvent(self, event):
        # Para a câmera quando o formulário é fechado
        self.camera.release()
        event.accept()


if __name__ == "__main__":
    app = Cancela_Tab(sys.argv)  # chama a classe "Cancela_Tab" que cancela a ação da tecla Tab
    window = J_FormCapturaImagemCliente()
    window.show()
    sys.exit(app.exec_())

