








consumo = float(input("Digite a quantidade de kWh consumida: "))
tipo_instalacao = input("Digite o tipo de instalação (R para Residencial, I para Industrial, C para Comercial): ").upper()

if tipo_instalacao == 'R':
    if consumo <= 500:
        preco = consumo * 0.40
    else:
        preco = consumo * 0.65
elif tipo_instalacao == 'C':
    if consumo <= 1000:
        preco = consumo * 0.55
    else:
        preco = consumo * 0.60
elif tipo_instalacao == 'I':
    if consumo <= 5000:
        preco = consumo * 0.55
    else:
        preco = consumo * 0.60
else:
    preco = "Tipo de instalação inválido."

if isinstance(preco, float):
    print(f"Preço a pagar: R$ {preco:.2f}")
else:
    print(preco)




















