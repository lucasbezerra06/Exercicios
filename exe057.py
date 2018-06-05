s = ''
while 'M' != s != 'F':
    s = str(input('Ditite o seu sexo [M/F]: ')).upper()
    if 'M' != s != 'F':
        print('=-'*20)
        print('Opção invalida!!')
        print('=-'*20)
print('Seu sexo é masculino' if s == 'M' else 'Seu sexo é feminino')

