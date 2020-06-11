class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Digite um número de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Número não pode ser maior que 10.')
        elif x < 0:
            raise InputError('Número não pode ser menor que 0.')
        break
    except ValueError:
        print('Digite apenas números!')