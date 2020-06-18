#Informando comando importado
from datetime import date , time, datetime
print()

def job_date ():
    #Formatação de data
    data_atual = date.today()
    #print(data_atual)
    #Formatação da data simbolos
    print('Data: {}'.format(data_atual.strftime('%d / %A / %B / %Y')))

def job_time():
    #Formatação de hora
    horario = time(hour= 15 , minute= 18 , second= 30)
    print('Hora: {}'.format(horario.strftime('%H : %M : %S')))

if __name__ == '__main__':
    job_date()
    job_time()
