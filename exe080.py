lista = list()
for c in range(0, 5):
    ultimo = True
    valor = int(input('Digite um valor: '))
    for c, v in enumerate(lista):
        if v > valor:
            lista.insert(c, valor)
            ultimo = False
            print(f'Adicionado na posição {c} da lista...')
            break
    if ultimo == True:
        lista.append(valor)
        print('Adicionado no final da lista...')
print(f'Os valores digitados em ordem foram {lista}')