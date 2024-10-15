macas = int(input("quantas maças deseja comprar?"))

if macas < 12:
    preco = 0.30
else:
    preco = 0.25

valor = macas * preco
print(f"Valor total: R$ {valor:2f}")