texto = 'Python' # tupla('P', 'y', 't', 'h', 'o', 'n')

# imprimir letra da string com índice
print(texto[3])

# imprimir a última letra com índice
print(texto[-1])

# erro ao tentar atribuir um valor à tupla
#texto[3] = 't'

# é imutável, mas posso trocar o valor inteiro
texto = 'Pythonia'
print(texto)

# .find - retorna o índice do texto desejado
# obs.: retorna -1 caso não encontre o texto
print(texto.find('n')) #5
print(texto.find('f')) #-1

# .index - retorna o índice do texto desejado
# obs.: retorna ValueError caso não encontre o texto
print(texto.index('n')) #5
#print(texto.index('f')) #-1

#  replace - substitui valor na string
novo_texto = texto.replace('P', 'p')
print(novo_texto)
print(texto)

# in
#for letra in texto:
#    print(letra)

frase = 'gatos são melhores que cachorros'
pesquisa = 'chor'
if pesquisa in frase:
    print(frase.index(pesquisa))
else:
    print(f'{pesquisa} não foi encontrado...')

frase = 'a rápida raposa marrom pula sobre o cachorro preguiçoso'

# slicing - retorna uma substring com índice do começo e fim
subtexto = frase[9:15]
print(frase)

print(f'O texto {subtexto} está entre os índices 9 e 15')