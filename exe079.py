lista = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Valor dubplicado...')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    while True:
        op = str(input('Deseja sari? [S/N]: '))
        if op.upper()[0]  in 'SN':
            break
    if op.upper()[0] == 'S':
        break
print('=-' * 40)
print(f'Você digitou os valores {sorted(lista)}')
