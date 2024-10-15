def data_valida(dia, mes, ano):
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > 31:
        return False
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    if mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia > 29:
                return False
        elif dia > 28:
            return False
    return True

data_input = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = map(int, data_input.split('/'))

if data_valida(dia, mes, ano):
    print("Data válida.")
else:
    print("Data inválida.")