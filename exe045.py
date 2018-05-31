from random import randint
op = int(input('1 - pedra\n'
               '2 - papel\n'
               '3 - tesoura: '))
jokenpo = ['Pedra', 'Papel', 'Tesoura']
oppc = randint(1, 3)
print('{} X {}'.format(jokenpo[op-1], jokenpo[oppc-1]))
if op == oppc:
    print('Empate')
elif op-oppc == (-2) or op-oppc == 1:
    print('Você venceu!')
else:
    print('Você perdeu!')
