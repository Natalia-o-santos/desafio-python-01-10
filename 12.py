num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Lê a operação desejada
operacao = input("Qual operação você deseja realizar (+, -, *, /): ")

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero."
else:
    resultado = "Operação inválida."

print(f"Resultado: {resultado}")