dis = float(input('Digite a distância da viagem: '))
if dis > 200:
    pas = dis * 0.45
else:
    pas = dis * 0.50
print('O preço da passagem é de R${}, por percorrer {}Km'.format(pas, dis))
