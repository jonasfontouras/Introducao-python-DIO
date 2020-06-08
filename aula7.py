#Utilização de métodos e funções no Python
#Utilização de classes

#Função:
### def função(a, b):
        #return a + b
def soma(a,b):
    return a + b

def multiplicacao(a, b):
    return a * b

def subtracao(a, b):
    return a - b

def divisao(a, b):
    return a / b

a = int(input("A: "))
b = int(input("B: "))

print(soma(a,b))
print(subtracao(a,b))
print(multiplicacao(a,b))
print(divisao(a,b))

#---------------------------------------
class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 7

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            print("Ligue a TV para trocar de canal")
        else:
            self.canal += 1
    
    def diminui_canal(self):
        if self.ligada:
            print("Ligue a TV para trocar de canal")
        else:
            self.canal -= 1
    

televisao = Televisao()
print("TV ligada: {}".format(televisao.ligada))
televisao.power()
televisao.aumenta_canal()
print("TV ligada: {}".format(televisao.ligada))
televisao.power()