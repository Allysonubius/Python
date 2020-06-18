#Personalização
print('Nota de alunos 0 a 10')
class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

#Excptions While
while True:
    try:
        x = int(input('Insira a nota: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser acima de 10 !')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0 !')
        break
    except ValueError:
        print('Somente N°s !')
    except InputError as ex:
        print(ex)