letra = input("Digite uma letra: ").lower()

if letra in 'aeiou':
    print("A letra é uma vogal.")
elif letra.isalpha() and len(letra) == 1:  # Verifica se é uma letra
    print("A letra é uma consoante.")
else:
    print("Entrada inválida. Por favor, insira apenas uma letra.")