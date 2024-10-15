valor_compra = float(input("Digite o valor de compra do produto: "))

if valor_compra < 20.00:
    valor_venda = valor_compra * 1.45  # 45% de lucro
else:
    valor_venda = valor_compra * 1.30  # 30% de lucro

print(f"Valor de venda: R$ {valor_venda:.2f}")