diretorio = 'C:/Users/jonas/OneDrive/Área de Trabalho/PythonClass/Introducao-python-DIO/teste.txt'

def escreve_arquivo(texto):
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualiza_arquivo(texto):
    arquivo = open(diretorio, 'a')
    arquivo.write(texto)
    arquivo.close()

def read_arquive():
    arquivo = open(diretorio, 'r')
    texto = arquivo.read()
    print(texto)
    arquivo.close()

if __name__ == "__main__":
    pass
    condicao1 = str(input('Anotar algo? '))
    if condicao1 == 'sim':
        anotacao = str(input('Anotação: '))
        escreve_arquivo('\n{}'.format(anotacao))
        condicao2 = str(input('Deseja anotar algo mais? '))
        while condicao2 == 'sim':
            anotacao = str(input('Anotação: '))
            atualiza_arquivo('\n{}'.format(anotacao))
            condicao2 = str(input('Deseja anotar algo mais? '))

    condicao3 = str(input('Deseja ler o arquivo?: '))
    if condicao3 == 'sim':
        read_arquive()