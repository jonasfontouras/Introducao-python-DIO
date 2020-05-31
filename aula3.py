a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
c = int(input("Digite um valor para c: "))

if a > b and a > c:
    print("valor de {} é maior".format(a))
elif b > a and b > c:
    print("valor de {} é maior".format(b))
else:
    print("valor de {} é maior".format(c))

print('Final do programa')#Aparecerá mesmo se a condição acima não for verdadeira, pois não está no mesmo bloco de codigo
#Inicio e fim de um bloco através da identação
