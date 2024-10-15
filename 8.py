time1 = int(input("Digite a quantidade de gols do primeiro time: "))
time2 = int(input("Digite a quantidade de gols do segundo time: "))

if time1 > time2:
    print("Vitória do primeiro time.")
elif time1 < time2:
    print("Vitória do segundo time.")
else:
    print("Empate.")