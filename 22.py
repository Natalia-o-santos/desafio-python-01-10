precos = {
    "file": (4.90, 5.80),
    "alcatra": (5.90, 6.80),
    "picanha": (6.90, 7.80)
}

# Lê o tipo de carne e a quantidade
tipo_carne = input("Digite o tipo de carne (file, alcatra, picanha): ").strip().lower()
quantidade = float(input("Digite a quantidade em Kg: "))
pagamento_cartao = input("Pagamento no cartão Tabajara? (s/n): ").strip().lower()

# Verifica se o tipo de carne é válido
if tipo_carne in precos:
    preco_kg = precos[tipo_carne][0] if quantidade <= 5 else precos[tipo_carne][1]
    valor_total = preco_kg * quantidade
    desconto = 0.05 * valor_total if pagamento_cartao == 's' else 0
    valor_a_pagar = valor_total - desconto

    # Exibe o cupom fiscal
    print("\n--- Cupom Fiscal ---")
    print(f"Tipo de carne: {tipo_carne.capitalize()}")
    print(f"Quantidade: {quantidade:.2f} Kg")
    print(f"Preço total: R$ {valor_total:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
else:
    print("Tipo de carne inválido.")