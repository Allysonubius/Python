##IMPORTAÇÂO DE OUTROS ARQUIVOS
from Aula7_televisao import Televisao
from Aula7_calculadora_1 import Calculadora
from Aula8_contador_letras import contador_letras

if __name__ == '__main__':
    #CLASSES IMPORTADAS TELEVISAO
    televisao = Televisao()
    televisao.power()
    print(televisao.ligada)
    print('----------- x -----------')
    print(televisao.ligada)
if __name__ == '__main__':
    #CLASSES IMPORTADAS CALCULDADORA
    print('----------- x -----------')
    calculadora = Calculadora(5,10)
    print(calculadora.soma())

if __name__ == '__main__':
    #CONTADOR DE LETRAS
    print('----------- x -----------')
    lista = ['cachorro', 'gato', 'elefante']
    print('A palavra {} contém {} letras'.format(lista[0],contador_letras(lista[0])))
    print('----------- x -----------')
    lista = ['cachorro', 'gato', 'elefante']
    print('A palavra {} contém {} letras'.format(lista[1], contador_letras(lista[1])))
    print('----------- x -----------')
    lista = ['cachorro', 'gato', 'elefante']
    print('A palavra {} contém {} letras'.format(lista[2], contador_letras(lista[2])))
    ##TOTAL DE LETRAS DA LISTA
    print('----------- x -----------')
    total_letras = contador_letras(lista)
    print('O total de letras da lista {} '.format(total_letras))