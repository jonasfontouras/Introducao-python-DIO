conjuntoA = {1, 2, 3, 4}
conjuntoB = {4, 5, 6}
ConjuntoC = {15, 16, 17, 18, 19}
ConjuntoD = {17, 18, 19}
lista = [9, 10, 11, 10, 11]

conjuntoB.add(7)
conjuntoA.discard(1)

uniaoAB = conjuntoA.union(conjuntoB)
print('A união com B: {}'.format(uniaoAB))

interseccaoAB = conjuntoA.intersection(conjuntoB)
print('A intersecção com B: {}'.format(interseccaoAB))

diferencaAB = conjuntoA.difference(conjuntoB)   
print('A diferenca em B: {}'.format(diferencaAB))

symetricAB = conjuntoA.symmetric_difference(conjuntoB)
print('A Diferença Simétrica em B: {}'.format(symetricAB))

subconjCD = ConjuntoD.issubset(ConjuntoC)
print('D é subconjunto do conjunto C: {}'.format(subconjCD))
superconjCD = ConjuntoC.issuperset(ConjuntoD)
print('C é superconjunto do conjunto D: {}'.format(superconjCD))

#Transformar lista p/ conjunto para remover elementos repetidos e depois reverter o mesmo para lista
print('Lista: {}'.format(lista))
conjuntlist = set(lista)
print('De lista para conjunto: {}'.format(conjuntlist))
listconjunt = list(conjuntlist)
print('De conjunto para lista: {}'.format(listconjunt))




