numero = int(input("Digite um número inteiro menor que 1000: "))

numero = int(input("Digite um número inteiro menor que 1000: "))

if numero < 0 or numero >= 1000:
    print("Número inválido. Deve ser menor que 1000.")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    resultado = ""

    # Construindo a mensagem
    if centenas > 0:
        resultado += f"{centenas} centena{'s' if centenas > 1 else ''}"

    if dezenas > 0:
        if resultado:  # Adiciona vírgula se já houver parte anterior
            resultado += ", "
        resultado += f"{dezenas} dezena{'s' if dezenas > 1 else ''}"

    if unidades > 0:
        if resultado:  # Adiciona vírgula se já houver parte anterior
            resultado += " e "
        resultado += f"{unidades} unidade{'s' if unidades > 1 else ''}"

    # Se o número for 0
    if numero == 0:
        resultado = "0 unidades"

    print(resultado)
