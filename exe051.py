pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
print('Progressão aritmetica de {} com razão {}'.format(pt, r))
for c in range(0, 11):
    pt += r
    print("{}".format(pt), end=',')
