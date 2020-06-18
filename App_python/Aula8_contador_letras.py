def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
       quant = len(x)
       contador.append(quant)
    return contador

if __name__ == '__main__':
    lista_1 = ['cachorro']
    lista_2 =  ['gato']
    print('A palavra {} contém {} letras'.format(lista_1,contador_letras(lista_1)))
    print('A palavra {} contém {} letras'.format(lista_2, contador_letras(lista_2)))