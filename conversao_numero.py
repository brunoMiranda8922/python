numero = int(input("Digite um numero inteiro: "))
print('''Converter numero para
[1] - Binário
[2] - Hexadecimal
[3] - Octal''')
opcao = int(input("Escolha uma das opções: "))
if opcao == 1:
    print(bin(numero)[2:])
elif opcao == 2:
    print(hex(numero)[2:])
elif opcao == 3:
    print(oct(numero)[2:])    
else:
    print("Opção inválida")
    