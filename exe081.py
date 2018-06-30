lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        op = str(input('Quer continuar? [S/N]: ')).upper()
        if op[0] in 'SN':
            break
    if op[0] == 'N':
        break
print('=-'*30)
print(f'Foram digitados {len(lista)} números')
descrescente = sorted(lista, reverse=True)
print(f'Lista de valores ordenada de forma decrescente: {descrescente}')
if 5 in lista:
    print('O valor 5 esta na lista...')
else:
    print('O valor 5 não esta na lista...')
