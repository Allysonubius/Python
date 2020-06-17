print()
#Interação com usuario
a = int(input('Insira um valor:'))
b = int(input('Insira outro:'))
print()
#Calculos
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
modulo = a % b
#Impressão
print('Soma: {sum}'.format(sum=soma))
print('Subtração: {sub}'.format(sub=subtracao))
print('Multiplicação: {mult}'.format(mult=multiplicacao))
print('Divisão: {div}'.format(div=divisao))
print('Resto: {mod}'.format(mod=modulo))

a = 10/2
b = 10 % 2
print(a,b)