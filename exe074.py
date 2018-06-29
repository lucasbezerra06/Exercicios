from random import randint
'''num = randint(0, 10)
num2 = randint(0, 10)
num3 = randint(0, 10)
num4 = randint(0, 10)
num5 = randint(0, 10)'''
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: {tupla}')
'''maior = tupla[0]
menor = tupla[0]
for c in range(1, len(tupla)):
    if tupla[c] > maior:
        maior = tupla[c]
    elif tupla[c] < menor:
        menor = tupla[c]'''

print(f'O maior valor sorteado foi: {max(tupla)}')
print(f'O menor valor sorteado foi: {min(tupla)}')


