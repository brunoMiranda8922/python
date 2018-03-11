valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite seu salário: "))
quantos_anos = int(input("Em quantos anos pretende pagar? "))

prestacao = valor_casa / (quantos_anos * 12) 
mininimo = salario * 0.3
print("Para pagar o valor da casa {} em {} anos".format(valor_casa,quantos_anos))
print("Prestação será de R$ {:.2f} ao mês".format(prestacao))
if prestacao > mininimo:
    print("Emprestimo negado")
else:
    print("Emprestimo aprovado")


