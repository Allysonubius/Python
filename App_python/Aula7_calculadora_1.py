# Metodos e Definições
class Calculadora :
    #Metodo
    def __init__(self, num1 , num2):
        self.valor_a = num2
        self.valor_b = num2
    #METODOS DE CALCULOS
    #SOMA
    def soma (self):
        return self.valor_a + self.valor_b
    #SUBT
    def subt (self):
        return self.valor_a - self.valor_b
    #MULT
    def mult (self):
        return self.valor_a * self.valor_b
    #DIV
    def divi (self):
        return self.valor_a / self.valor_b
#MAIN
if __name__ == '__main__':
    #INSTANCIANDO METODO CALCULADORA
    print()
    calculadora = Calculadora(10,2)
    print('SOMA: {}'.format(calculadora.soma()))
    print('SUBTRAÇÂO: {}'.format(calculadora.subt()))
    print('MULTIPLICAÇÂO: {}'.format(calculadora.mult()))
    print('DIVISÂO: {}'.format(calculadora.divi()))
