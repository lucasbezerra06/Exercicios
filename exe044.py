precoNormal = float(input('Digite o preço normal do produto: '))
forma = int(input('Forma de pagamento\n'
                  '1 - A vista\n'
                  '2 - cartão: '))
if forma == 1:
    porção = 10
    novo = precoNormal - precoNormal * porção / 100
    tipo = str('com desconto de {}%'.format(porção))
else:
    vezes = int(input('Quantas vezes? 0 para pagamento a vista: '))
    if vezes == 0:
        porção = 5
        novo = precoNormal - precoNormal * porção / 100
        tipo = str('com desconto de {}%'.format(porção))

    elif vezes <= 2:
        novo = precoNormal
        tipo = str('')

    else:
        porção = 20
        novo = precoNormal + precoNormal * porção / 100
        tipo = str('com juros de {}%'.format(porção))

print('O novo preço do produto é RS{:.2f} {}'.format(novo, tipo))
