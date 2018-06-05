pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = pt + (10 - 1) * r
print('Progresssão aritmetica de {} com razão {}'.format(pt, r))
while pt < decimo + r:
    print('{}'.format(pt), end=' -> ')
    pt += r
print('FIM')
