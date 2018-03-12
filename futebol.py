def calcular_pontos (): 
    time = input("Digite seu time: ")
    vitoria = int(input("Digite a quantidade de vitórias: "))
    empates = int(input("Digite a quantidade de empates: "))
    derrotas = int(input("Digite a quantidade de derrotas: "))
    resultado = (vitoria * 3) + empates
    return [time, resultado]


time1 = calcular_pontos()

time2 = calcular_pontos() 

if time1[1] > time2[1]:
    print("{} venceu com {} pontos".format(time1[0], time1[1]))
elif time1[1] == time2[1]:
    print("Deu empate")
else: 
     print("{} venceu com {} pontos".format(time2[0], time2[1]))


