#19 e 20
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Não existem raízes reais.")
elif delta == 0:
    raiz = -b / (2 * a)
    print(f"Existem raízes reais idênticas: {raiz:.2f}")
else:

    raiz1 = (-b + (delta ** 0.5)) / (2 * a)
    raiz2 = (-b - (delta ** 0.5)) / (2 * a)
    print(f"Existem raízes reais distintas: {raiz1:.2f} e {raiz2:.2f}")