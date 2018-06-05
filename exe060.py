n = int(input('Digite um número: '))
strFat = '{}'.format(n)
i = n
fat = n
while i > 1:
    i -= 1
    fat *= i
    strFat += ' X {}'.format(i)
print('{}! = {} = {}'.format(n, strFat, fat))
