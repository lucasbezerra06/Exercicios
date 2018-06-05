from random import randint
from time import sleep
num = 11
tentativa = 0
print('Pensando...')
sleep(1)
comp = randint(0, 10)
while comp != num:
    num = int(input('Digite um número entre 0 e 10: '))
    if 0 < num > 10:
        print('Numero invalido')
        print('=-' * 20)
    elif num == comp:
        print('Você venceu!')
        print('=-' * 20)
        tentativa += 1
    else:
        print('Voce perdeu!')
        print('=-' * 20)
        tentativa += 1
print('Você acertou na {}º tentativa.'.format(tentativa))



