tabela = ('Flamengo', 'Atlético Mineiro', 'São Paulo', 'Internacional', 'Grêmio',
          'Palmeiras', 'Sport Recife', 'Cruzeiro', 'Botafogo',
          'Corinthians', 'Vasco', 'Fluminense', 'America-mg', 'Chapecoense',
          'Santos', 'Vitória', 'Bahia', 'Paraná', 'Atlético-pr', 'Ceará')
print("=-"*15)
print(f'Os cinco primeiros colocados são: {tabela[0:5]}')
print("=-"*15)
print(f'Os últimos 4 colocados são: {tabela[-4:]}')
print("=-"*15)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print("=-"*15)
chapeco = tabela.index('Chapecoense' ) + 1
print(f'Posição da chapecoense é: {chapeco}')