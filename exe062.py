pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
quant = 10
decimo = pt + (quant - 1) * r
print('Progresão aritmetica de {} com razão {}'.format(pt, r))
c = pt
while quant != 0:
    if c < decimo + r:
        print('{}'.format(c), end=' -> ')
        c += r
    else:
        print('FIM')
        print('-=' * 30)
        quant = int(input('Quantos termos a mais você deseja exibir? '))
        decimo = pt + ((10 + quant) - 1) * r
print('Fim do programa!')
