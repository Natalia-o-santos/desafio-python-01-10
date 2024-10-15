#4 e 5
lados = int(input("Digite o número de lados do polígono: "))
medidaLado = float(input("Digite a medida do lado em cm: "))

match lados:
    case 3:
        area = (medidaLado ** 2 * (3 ** 0.5)) / 4  # Área do triângulo
        print(f"TRIÂNGULO\nÁrea: {area:.2f} cm²")
    case 4:
        area = medidaLado ** 2  # Área do quadrado
        print(f"QUADRADO\nÁrea: {area:.2f} cm²")
    case 5:
        print("PENTÁGONO")
    case _ if lados < 3:
        print("NÃO É UM POLÍGONO")
    case _ if lados > 5:
        print("POLÍGONO NÃO IDENTIFICADO")
