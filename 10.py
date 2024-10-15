I = int(input("Digite um valor I (inteiro positivo): "))
A = float(input("Digite o valor A: "))
B = float(input("Digite o valor B: "))
C = float(input("Digite o valor C: "))

if I % 2 == 0:  # Se I é par
    media_aritmetica = (A + B + C) / 3
    print(f"Média aritmética: {media_aritmetica:.2f}")
elif I > 10:  # Se I é ímpar e maior que 10
    media_ponderada = (A * 2 + B * 3 + C * 4) / (2 + 3 + 4)
    print(f"Média ponderada: {media_ponderada:.2f}")
else:
    print("O valor de I não atende aos critérios.")