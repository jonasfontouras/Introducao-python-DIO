a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
c = int(input("Digite um valor para c: "))

resto_a = a % 2
resto_b = b % 2
resto_c = c % 2
cont_par = 0
cont_impar = 0

if a > b and a > c:
    print("valor de {} é maior".format(a))
elif b > a and b > c:
    print("valor de {} é maior".format(b))
else:
    print("valor de {} é maior".format(c))

if resto_a == 0:
    cont_par = cont_par + 1
else:
    cont_impar = cont_impar + 1

if resto_b == 0:
    cont_par = cont_par + 1
else:
    cont_impar = cont_impar + 1

if resto_c == 0:
    cont_par = cont_par + 1
else:
    cont_impar = cont_impar + 1

print("Há {} números pares".format(cont_par))
print("Há {} números ímpares".format(cont_impar))

print('Final do programa')#Aparecerá mesmo se a condição acima não for verdadeira, pois não está no mesmo bloco de codigo
#Inicio e fim de um bloco através da identação
