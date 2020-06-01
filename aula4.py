#Laços de repetição: FOR, WHILE e Comando RANGE

#--------------Números primos com o comando FOR--------------------
f = int(input("Entre com um número: "))

for num in range(f+1):
    div = 0 
    for x in range(1, num+1):
        resto = num % x
        if resto == 0:
            div += 1
    if div == 2:
        print(num)


#--------------Números primos com o comando WHILE------------------
nota1 = int(input("Nota 1 (de 0 a 10):"))
while nota1 > 10: 
    nota1 = int(input("Valor inválido. Nota 1 (de 0 a 10):"))
nota2 = int(input("Nota 2 (de 0 a 10):"))
while nota2 > 10: 
    nota2 = int(input("Valor inválido. Nota 2 (de 0 a 10):"))
nota3 = int(input("Nota 3 (de 0 a 10):"))
while nota3 > 10: 
    nota3 = int(input("Valor inválido. Nota 3 (de 0 a 10):"))

media = (nota1 + nota2  +nota3) / 3
print(media)