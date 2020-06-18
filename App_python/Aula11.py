#LISTA
lista = [1,10]
#Fazendo um erro
try:
    div = 10 /0
    num = lista[3]
#Encadeamento de exccetion
except ZeroDivisionError:
    print('Não e possivel realizar uma divisão por 0 !')
except WindowsError:
    print('Erro ao acessar o indice invalido da lista !')
except BaseException as ex:
    print('Erro desconhecido {}'.format(ex))
else:
    print('Executa quando não ocrre erro !')