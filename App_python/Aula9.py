#ESCRITA DO ARQUIVO
def escrever_arquivo(texto):
    #Iniciando
    arquivo = open('teste.txt','w')
    #escrevendo no arquivo
    arquivo.write(texto)
    arquivo.close()
#ATUALIZAÇÂO DO ARQUIVO
def atualizar_arquivo(texto):
    arquivo = open('teste.txt','a')
    arquivo.write(texto)
    arquivo.close()
#LEITURA
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)
#REFACTOR
if __name__ == '__main__':
    #escrever_arquivo('Primeira linha \n')
    #atualizar_arquivo('Segunda linha \n')
    ler_arquivo('teste.txt')