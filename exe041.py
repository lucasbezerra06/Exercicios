from datetime import date
nasci = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nasci
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
