lista = [7, 8, 1, 2, 4, 6]
lista_animal = ['Cachorro', 'Gato', 'Peixe'] 

#Condicional com lista
animal = str(input("Digite um animal: "))

#Procura animal na lista
if animal in lista_animal:
    condicao1 = str(input("{} está na lista. Deseja excluir?\n".format(animal)))
    #Condicional para remover animal da lista ou não
    if condicao1 == 'sim':
        lista_animal.remove(animal) #Remove animal
        print('Fim do programa. Lista: ')
        lista_animal.sort() #Ordena a lista
#Condicional para adicionar animal na lista ou não
else:
    condicao2 = str(input("{} não esta na lista, deseja incluir?\n ".format(animal)))
    if condicao2 == 'sim':
        lista_animal.append(animal) #Adiciona animal
        lista_animal.sort() #Ordena a lista
    else:
        print('Fim do programa. Lista: ')

#Laço de repetição para apresentar os elementos da tela 
for x in lista_animal:
    print(x)



#---------------
num = int(input("Digite um número: "))
condicao = str(input("Deseja adicionar mais um numero?"))

while condicao == 'sim':
    num = int(input("Digite um número: "))
    lista.append(num)
    condicao = str(input("Deseja adicionar mais um numero?"))
lista.sort()
for z in lista:
    print(z)
cond = str(input('Sua lista está ordenada. Deseja reverter?'))
if cond == 'sim':
    lista.reverse()
    print('Lista reversa:')
    for y in lista:
        print(y)