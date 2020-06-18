class Televisao :
    #CONFIGURAÇÔES DO CONTROLE
    def __init__(self):
        self.ligada = False
        self.camal = 2
    #BOTAO LIGA E DESLIGA CONTROLE
    def power (self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    #BOTAO PARA MUDAR CHANELS
    def aumenta_canal (self):
        if self.ligada:
            self.camal += 2
    def diminui_canal(self):
        if self.ligada:
            self.camal -= 2
print('----------- x -----------')
print(__name__)
#MAIN
if __name__ == '__main__':
    #TESTANDO BOTÂO LIGAR E DESLIGAR
    print('----------- x -----------')
    televisao = Televisao()
    print('Desligada {}'.format(televisao.ligada))
    televisao.power()
    print('Ligada {}'.format(televisao.ligada))
    televisao.power()
    print('Desligada {}'.format(televisao.ligada))
    televisao.power()
    print('Ligada {}'.format(televisao.ligada))
    #BOTAO DE MUDAR DE CANAIS
    print('----------- x -----------')
    print('Canal {}'.format(televisao.camal))
    televisao.aumenta_canal()
    print('Proximo Canal {}'.format(televisao.camal))
    televisao.diminui_canal()
    print('Canal Anterior {}'.format(televisao.camal))
print('----------- x -----------')