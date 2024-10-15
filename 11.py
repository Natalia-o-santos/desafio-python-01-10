numeros = []

# Lê 10 números inteiros
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

valor_maximo = max(numeros)
valor_minimo = min(numeros)
valor_medio = sum(numeros) / len(numeros)

print(f"Valor máximo: {valor_maximo}")
print(f"Valor mínimo: {valor_minimo}")
print(f"Valor médio: {valor_medio:.2f}")