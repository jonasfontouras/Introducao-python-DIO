#jogo da velha faz comentários no código
a = 10
b = 5   
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

resultado = ('Soma: {soma}'
             '\nSubtração: {sub}'
             '\nMultiplicação: {mult}'
             '\nDivisão: {div}'
             '\nResto: {resto}'.format(soma=soma,
                                        sub=subtracao,
                                        mult=multiplicacao,
                                        div=divisao,
                                        resto=resto))        

print(resultado)
