n = int(input('Digite um número: '))
cont = 0
for c in range(1, n):
    if n % c == 0:
        cont += 1
if cont > 1:
    print('O número {} não é primo'.format(n))
else:
    print('O número {} é primo'.format(n))
