expressao = str(input('Digite uma expressão: '))
parenteses = 0
for c in expressao:
    if c == '(':
        parenteses += 1
    if c == ')':
        parenteses -= 1
if parenteses == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
