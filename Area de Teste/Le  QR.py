from pyzbar import pyzbar
from PIL import Image


def ler_qr_code(nome_arquivo):
    imagem = Image.open(nome_arquivo)
    resultado = pyzbar.decode(imagem)

    if len(resultado) == 0:
        print("Nenhum código QR encontrado na imagem.")
        return None

    return resultado[0].data.decode("utf-8")


nome_arquivo = input("Digite o nome do arquivo de imagem contendo o QR code: ")

texto = ler_qr_code(nome_arquivo)
if texto:
    print("Conteúdo do QR code:", texto)
