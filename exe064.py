n = 0
quant = 0
soma = 0
while n != 999:
    n = int(input('Digite um número inteiro, digite 999 para sair: '))
    if n != 999:
        quant += 1
        soma += n
print('Quantidade de números digitados: {}\nSoma dos números digitados: {}'.format(quant, soma))
