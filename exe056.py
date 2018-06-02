media = 0
mv = 0
nomeHM = str('')
quantMulheMeno = 0
for i in range(0, 4):
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite seu sexo(M ou F): ')).upper()
    print('-=' * 30)
    media += idade
    if i == 0 and sexo == 'M':
        mv = idade
        nomeHM = nome
    elif idade > mv and sexo == 'M':
        mv = idade
        nomeHM = nome
    if idade < 20 and sexo == 'F':
        quantMulheMeno += 1
media = media / 4
print('Média de idade do grupo: {:.0f} anos.'.format(media))
print('O nome do homem mais velho é {} com {} anos.'.format(nomeHM, mv))
print('Quantidade de mulheres com menos de 20 anos: {}.'.format(quantMulheMeno))