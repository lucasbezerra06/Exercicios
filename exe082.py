lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        op = str(input('Deseja continuar? [S/N]: ')).upper()
        if op[0] in 'SN':
            break
    if op[0] == 'N':
        break
pares = list()
impares = list()
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print('=-' * 30)
print(f'Lista completa: {lista}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')
