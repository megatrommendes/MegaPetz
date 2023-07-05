import qrcode


def gerar_qr_code(texto, nome_arquivo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    imagem = qr.make_image(fill_color="black", back_color="white")
    imagem.save(nome_arquivo)


texto = input("Digite o texto para gerar o QR code: ")
nome_arquivo = input("Digite o nome do arquivo de imagem: ")

gerar_qr_code(texto, nome_arquivo)
