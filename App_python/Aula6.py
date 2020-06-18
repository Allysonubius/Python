# LISTA[]
# TUPLA()
# CONJUNTO {}
#INICIANDO CONJUNTO 1
conjunto1 = {1,2,3,4}
#IMPRESSÂO
print()
print('Conjunto : {}'.format(conjunto1))
#Inserindo
conjunto1.add(5)
#Discartando
conjunto1.discard(3)
#Impressão
print('Conjunto deletado n° 3: {}'.format(conjunto1))
#INICIANDO CONJUNTO 2
conjunto2 = {5,6,7,8,9}
#UNINDO os conjuntos
uniao = conjunto1.union(conjunto2)
#Impressão da união de conjuntos
print()
print("Unidos os 2 conjuntos : {}".format(uniao))
print()
# Impressão do N° de conjuntos em interseção
conjunto_interseção = conjunto1.intersection(conjunto2)
print('Interseção ou repetido : {}'.format(conjunto_interseção))
#Diferença entre conjuntos:
print()
conjutos_1 = conjunto1.difference(conjunto2)
conjutos_2 = conjunto2.difference(conjunto1)
print('O conjunto {}  e diferente do conjunto {}'.format(conjunto1, conjunto2))
#Diferença simetrica
print()
conjunto_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferença simétrica: {} ' .format(conjunto_simetrica))
#Ele verifica se o conjunto contém os mesmos números em outro conjunto
print()
conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
##ISSUBSET
print()
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('O conjunto {} contém o conjunto {} sendo então {}'.format(conjunto_a,conjunto_b,conjunto_subset))
conjunto_subset = conjunto_b.issubset(conjunto_a)
print('O conjunto {} não contém o conjunto {} sendo então {}'.format(conjunto_b,conjunto_a,conjunto_subset))
##ISSUPERSET
print()
conjunto_subset = conjunto_a.issuperset(conjunto_b)
print('O superconjunto {} de {} sendo então {}'.format(conjunto_a,conjunto_b,conjunto_subset))
conjunto_subset = conjunto_b.issuperset(conjunto_a)
print('O superconjunto {} de {} sendo então {}'.format(conjunto_b,conjunto_a,conjunto_subset))