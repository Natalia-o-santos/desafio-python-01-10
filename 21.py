respostas_positivas = 0

# Perguntas sobre o crime
perguntas = [
    "Telefonou para a vítima ",
    "Esteve no local do crime?  ",
    "Mora perto da vítima?  ",
    "Devia para a vítima?  ",
    "Já trabalhou com a vítima?  "
]

# Faz as perguntas e conta as respostas positivas
for pergunta in perguntas:
    resposta = input(pergunta).strip().lower()
    if resposta == 's':
        respostas_positivas += 1

# Classificação com base nas respostas
match respostas_positivas:
    case 0 | 1:
        classificacao = "Inocente"
    case 2:
        classificacao = "Suspeita"
    case 3 | 4:
        classificacao = "Cúmplice"
    case 5:
        classificacao = "Assassino"

print(f"Classificação: {classificacao}")