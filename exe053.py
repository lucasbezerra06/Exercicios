frase = str(input('Digite uma frase: ')).strip()
nfrase = frase.replace(' ', '')
rfrase = str('')
for c in range(len(nfrase)-1, -1, -1):
    rfrase += nfrase[c]
if rfrase == nfrase:
    print('A frase {} é um palindromo'.format(frase))
else:
    print('A frase {} NÃO é um palindromo'.format(frase))

