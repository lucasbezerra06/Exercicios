palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
#print(len(palavras[4]))
for c in palavras:
    print(f'Na palavra {c.upper()} temos', end=' ')
    for l in range(0, len(c)):
        if c[l].upper() in 'AEIOU':
            print(c[l], end=' ')
    print()
