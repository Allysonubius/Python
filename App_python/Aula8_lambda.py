print('Aula8_lambda')
print('----------- x -----------')
#INICIO COM LAMBDA
contador_letras = lambda lista: [len(x) for x in lista]
#LISTAS
lista_animais = ['cat', 'dog', 'bird']
#Impressão
if __name__ == '__main__':
 print(contador_letras(lista_animais))
 print('----------- x -----------')
 print('A palavra {} contém {} letras'.format(lista_animais[0],contador_letras(lista_animais[0])))
 print('A palavra {} contém {} letras'.format(lista_animais[1],contador_letras(lista_animais[1])))
 print('A palavra {} contém {} letras'.format(lista_animais[2],contador_letras(lista_animais[2])))