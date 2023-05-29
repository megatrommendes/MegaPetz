def determinar_camada_atmosfera(altitude):
    if altitude <= 20:
        return "TROPOSFERA"
    elif altitude <= 50:
        return "ESTRATOSFERA"
    elif altitude <= 80:
        return "MESOSFERA"
    elif altitude <= 450:
        return "TERMOSFERA"
    else:
        return "EXOSFERA"

# Exemplo de uso
altitude = float(input("Digite a altitude em quilômetros: "))
camada = determinar_camada_atmosfera(altitude)
print(camada)