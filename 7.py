angulo1 = float(input("Digite o primeiro ângulo: "))
angulo2 = float(input("Digite o segundo ângulo: "))
angulo3 = float(input("Digite o terceiro ângulo: "))

soma_angulos = angulo1 + angulo2 + angulo3

if soma_angulos > 180:
    print("Os ângulos não formam um triângulo.")
else:
    if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        print("O triângulo é RETÂNGULO.")
    elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        print("O triângulo é OBTUSÂNGULO.")
    else:
        print("O triângulo é ACUTÂNGULO.")