dic = {"Nome": "Bruno", "Idade": "21 anos"}
print("Elementos do dic: ", dic, '\n') #Exibe todos os elementos do dic. (Chave: Valor)

print("Valores das chaves: ", dic["Nome"], dic["Idade"], '\n') #Retornando o valor associado à uma chave, notação de indices[]

dic["Nome"] = "Jose" #Atribuindo um novo valor na chave "Nome" 
print("Atribuindo um novo valor: ", dic["Nome"], dic["Idade"], '\n') 

dic["Nome2"] = "Messi" #Adicionando um novo Item ao dic, ["Chave"] = "Valor"
dic["Idade2"] = "22 anos" 
print("Adicionando um novo Item: ", dic["Nome"],dic["Idade"],',', dic["Nome2"], dic["Idade2"], '\n')

print("Tamanho do dic: ", len(dic), "elementos" , '\n') #Retorna o tamanho do dic 

del dic["Nome2"], dic["Idade2"] #Deleta um Item do dic
print("Item que não foi deletado: ", dic ,'\n')

existe_nome2 = "Nome2" in dic #Verifica se a chave "Nome2" existe em dic = False
print("Chave existe: ", existe_nome2, '\n')

existe_nome = "Nome" in dic #True
print("Chave existe: ", existe_nome,'\n')

chave_dic = dic.keys() #Utilizado p/ retornar as chaves do dic
print("Retornando as chaves do dic: ", chave_dic, '\n') 

valores_dic = dic.values() #Utilizado p/ retornar os valores do dic
print("Retornando os valores do dic: ", valores_dic, '\n') 

items_dic = dic.items() #Retorna os itens do dic em tuplas
print("Itens dic em tuplas: ",items_dic, '\n')

dic_valor = dic.get("Nome") #Retorna o valor a parti das chaves = Jose
print("Retorna o valor a parti das chaves: ", dic_valor, '\n')

dic_valor = dic.get("Nome2") #Caso chave não exista = None
print("Retorna o valor a parti das chaves: ",     dic_valor,'\n' )

            #Utilizando o for para percorrer cada item do dic 

for chave in dic: #Exibe o valor de cada item do dic
    print("Valor de cada item: ", dic[chave], '\n')
    
for chave, valor in dic.items(): #Exibe a chave e o valor de cada item do dic.
    print("Chave e Valor de cada item: ", chave, ':', valor)

