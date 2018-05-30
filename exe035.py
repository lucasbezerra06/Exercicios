r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if (r2 - r3) < r1 and r1 < (r2 + r3):
    if (r1 - r3) < r2 and r2 < (r1 + r3):
        if (r1 - r2) < r3 and r3 < (r1 + r3):
            print('As retas {}, {} e {} formam um triangulo!'.format(r1, r2, r3))
        else:
            print('As retas {}, {} e {} não formam um triangulo!'.format(r1, r2, r3))
    else:
        print('As retas {}, {} e {} não formam um triangulo!'.format(r1, r2, r3))
else:
    print('As retas {}, {} e {} não formam um triangulo!'.format(r1, r2, r3))
