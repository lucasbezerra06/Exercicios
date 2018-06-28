from random import randint
num = randint(0, 11)
num2 = randint(0, 11)
num3 = randint(0, 11)
num4 = randint(0, 11)
num5 = randint(0, 11)
tupla = (num, num2, num3, num4, num5)
maior = tupla[0]
menor = tupla[0]
print(f'Os valores sorteados foram: {tupla}')
for c in range(1, len(tupla)):
    if tupla[c] > maior:
        maior = tupla[c]
    elif tupla[c] < menor:
        menor = tupla[c]
print(f'O maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')


