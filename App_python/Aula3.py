#Interação com o usuario
a = int(input('1° bimestre: '))
if a > 10:
    a = int(input('Você digitou errado ! Digite o valor novamente :'))
b = int(input('2° bimestre: '))
if a > 10:
    a = int(input('Você digitou errado ! Digite o valor novamente :'))
c = int(input('3° bimestre: '))
if a > 10:
    a = int(input('Você digitou errado ! Digite o valor novamente :'))
d = int(input('4° bimestre: '))
if a > 10:
    a = int(input('Você digitou errado ! Digite o valor novamente :'))
#Calculo de média bimestral
media = (a + b + c + d) / 4
#Categorias de separação de medias dos alunos
if media >= 9:
    print("Voce está de parabéns ! {}".format(media))
elif media >= 7:
    print('Voce passou ! {}'.format(media))
elif media >= 5:
    print('Você passou com nota {} estude mais !'.format(media))
elif media <= 4:
    print('Você esta abaixo da média ! {}'.format(media))
elif media <=2 :
    print('Você não nota estude mais ! {}'.format(media))
#IF e ELSE
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     #impressão
#     print('media: {}'.format(media))
# else:
#     print('Foi informado alguma nota errada !')

# #Interação com o usuario
# a = int (input('Entre com 1° valor: '))
# b = int (input('Entre com 2° valor: '))
# #Modulo
# resto_a = a % 2
# resto_b = b % 2
# #Contestamento if e else
# if resto_a == 0 or not resto_b > 0:
#     print('Numero par !')
# else:
#     print('Nenhum numero par foi digitado !')

# #usuario
# a = input('Primeiro valor: ')
# b = input('Segundo valor: ')
# c = input('Terceiro valor:')
# print()
# #Conversão
# if a > b and a > c:
#     print('o maior número é {}'.format(a))
# elif b > a and b > c:
#     print('O maior número é {}'.format(b))
# else:
#     print('O maior número é {}'.format(c))
#     #Impressão
#     print('Finish !')