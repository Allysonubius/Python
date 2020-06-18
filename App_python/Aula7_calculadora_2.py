# Metodos e Definições
class Calculadora :
    # #Metodo
    # def __init__(self):
    #     pass
    #METODOS DE CALCULOS
    #SOMA
    def soma (self, valor_a , valor_b):
        return valor_a + valor_b
    #SUBT
    def subt (self, valor_a , valor_b):
        return valor_a - valor_b
    #MULT
    def mult (self, valor_a , valor_b):
        return valor_a * valor_b
    #DIV
    def divi (self, valor_a , valor_b):
        return valor_a / valor_b

#INSTANCIANDO METODO CALCULADORA
print()
calculadora = Calculadora()
print('SOMA: {}'.format(calculadora.soma(10,2)))
print('SUBTRAÇÂO: {}'.format(calculadora.subt(12,2)))
print('MULTIPLICAÇÂO: {}'.format(calculadora.mult(10,2)))
print('DIVISÂO: {}'.format(calculadora.divi(2,10)))