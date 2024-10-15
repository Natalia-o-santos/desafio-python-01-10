from datetime import datetime

# Solicita a data de nascimento
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = map(int, data_nascimento.split('/'))
nascimento = datetime(ano, mes, dia)

idade = (datetime.now() - nascimento).days // 365

if idade >= 18:
    print("Você pode votar.")
else:
    print("Você não pode votar.")
