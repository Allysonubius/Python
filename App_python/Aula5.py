#Inicio de uma Lista
lista = [1,3,5,7]
lista_animal = ['cachorro', 'gato', 'elefante']
#Impressão das listas
print(lista)
print(lista_animal)
print('-------------------------------------')
#Soma da Lista com números !
print('SOMA: ')
print(sum(lista))
print('MAX: ')
print(max(lista))
print('MIN: ')
print(min(lista))
print('-------------------------------------')
#Segmento da lista
if 'gato' in lista_animal:
    print('Existe um gato na lista')
else:
    print('Não existe na lista. O logo será incluido !')
    lista_animal.append('lobo')
    print(lista_animal)
print()
#lista_animal.pop('lobo')
# em ordem a lista
lista.sort()
lista_animal.sort()
print('Ordem crescente {}'.format(lista))
print('Ordem alfabetica {}'.format(lista_animal))