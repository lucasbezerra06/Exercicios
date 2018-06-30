valores = list()
for i in range(0, 5):
    valores.append(int(input(f'Digite o {i}º valor: ')))
maior = max(valores)
menor = min(valores)
print(f'O maior valor foi {maior} na posição', end=' ')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}...', end=' ')
print(f'\nO menor valor foi {menor} na posição', end=' ')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}...', end=' ')

