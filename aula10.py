from datetime import date, time, timedelta, datetime

def working_with_datetime():
    horario_zulu = str(input("Digite o horario zulu: "))
    zulu_convert = datetime.strptime(horario_zulu, '%H')
    horario_local = zulu_convert - timedelta(hours=3)
    print('Horário local: {}'.format(horario_local))

if __name__ == "__main__":
    working_with_datetime()