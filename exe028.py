import random
n = int(random.uniform(0, 5))
num = int(input('Digite um número entre 0 e 5: '))
if num == n:
    print('Você venceu!')
else:
    print('Você perdeu!')
