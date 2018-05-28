cidade = str(input('Digite o nome da cidade: '))
div = cidade.split()
if 'SANTOS' in div[0].upper():
    print('A cidade {} começa com o nome SANTOS'.format(cidade))
else:
    print('A cidade {} não começa com o nome SANTOS'.format(cidade))
