nome = input("Digite seu nome: ")
hora = int(input("Digite a hora atual (0-23): "))

if 5 <= hora < 12:
    mensagem = "Bom dia"
elif 12 <= hora < 18:
    mensagem = "Boa tarde"
else:
    mensagem = "Boa noite"

print(f"{mensagem}, {nome}!")