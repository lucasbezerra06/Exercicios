num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
num4 = int(input('Digite o quarto valor: '))
tupla = (num1, num2, num3, num4)
print(f'O número 9 aparece: {tupla.count(9)} veze(s)')
print(f'O digito 3 aparece na {tupla.index(3) + 1}ª posição')
print('Os números pares foram', end=' -> ')
for c in tupla:
    if c % 2 == 0:
        print(f'{c}', end=' ')

